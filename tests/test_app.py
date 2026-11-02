# [IA] Codex – Testes.
from pathlib import Path
import ast
import hashlib
import json
import os
import re
import sys
import unittest
from unittest.mock import patch

import pandas as pd
import streamlit as st
from streamlit.testing.v1 import AppTest

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))
from dados import (
    CSV_ORIGINAL, CSV_TRATADO, IMPUTAR, QUANTITATIVAS, carregar_dados,
    correlacionar, filtrar_intervalo, tratar_dados,
)


# [IA] Codex – Cache dos dados.
def arquivos_do_projeto():
    for pasta, diretorios, arquivos in os.walk(RAIZ):
        diretorios[:] = [nome for nome in diretorios if nome not in {'.git', '.venv', '__pycache__', '.pytest_cache'}]
        for nome in arquivos:
            yield Path(pasta) / nome


# [IA] Codex – Testes dos dados.
class TestDados(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = carregar_dados()

    def test_csv_eda(self):
        self.assertEqual(self.df.shape, (13397, 21))
        self.assertNotIn('match_id', QUANTITATIVAS)
        self.assertNotIn('yellow_card', QUANTITATIVAS)
        self.assertLess(self.df.player_name.nunique(), len(self.df))

    def test_preparacao_reproduzivel(self):
        if not CSV_ORIGINAL.exists():
            self.skipTest('CSV bruto não incluído no clone; consultar data/README.md.')
        original = pd.read_csv(CSV_ORIGINAL)
        copia = original.copy(deep=True)
        esperado = tratar_dados(original)
        pd.testing.assert_frame_equal(original, copia)
        pd.testing.assert_frame_equal(self.df, esperado)
        self.assertEqual(self.df[IMPUTAR].isna().sum().sum(), 0)

    def test_filtro_inclusivo_e_original_intacto(self):
        antes = self.df.copy(deep=True)
        recorte = filtrar_intervalo(self.df, 'age', (21, 23))
        self.assertTrue(recorte.age.between(21, 23).all())
        self.assertEqual(set(recorte.age), {21, 22, 23})
        recorte.loc[:, 'age'] = 0
        pd.testing.assert_frame_equal(self.df, antes)

    def test_filtro_vazio(self):
        vazio = filtrar_intervalo(self.df, 'age', (100, 110))
        self.assertTrue(vazio.empty)
        matriz, excluidas = correlacionar(vazio, ['age', 'goals'])
        self.assertTrue(matriz.empty)
        self.assertEqual(len(excluidas), 2)

    def test_filtros_invalidos(self):
        for coluna, intervalo in [('match_id', (1, 2)), ('age', (30, 20))]:
            with self.assertRaises(ValueError):
                filtrar_intervalo(self.df, coluna, intervalo)

    def test_spearman_ausentes_e_constantes(self):
        pequeno = pd.DataFrame({'age': [1, 2, 3, 4, None],
                               'goals': [2, 4, 6, 8, None],
                               'assists': [0, 0, 0, 0, 0]})
        matriz, excluidas = correlacionar(pequeno, ['age', 'goals', 'assists', 'match_id'])
        self.assertAlmostEqual(matriz.loc['age', 'goals'], 1)
        self.assertEqual(excluidas, ['assists'])
        self.assertNotIn('match_id', matriz)
        self.assertEqual(len(filtrar_intervalo(pequeno, 'age', (1, 4))), 4)

    def test_sem_selecao_e_poucos_pares(self):
        self.assertTrue(correlacionar(self.df, [])[0].empty)
        self.assertTrue(correlacionar(self.df.iloc[:2], ['age', 'goals'])[0].empty)

    def test_hash_tratado(self):
        manifesto = json.loads((RAIZ / 'data/proveniencia.json').read_text(encoding='utf-8'))
        self.assertEqual(hashlib.sha256(CSV_TRATADO.read_bytes()).hexdigest(), manifesto['sha256_tratado'])

    def test_sintaxe(self):
        for arquivo in arquivos_do_projeto():
            if arquivo.suffix == '.py':
                ast.parse(arquivo.read_text(encoding='utf-8'), filename=str(arquivo))

    def test_credenciais_conhecidas(self):
        padroes = [r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
                   r'gh[pousr]_[A-Za-z0-9]{30,}', r'AKIA[A-Z0-9]{16}', r'sk-[A-Za-z0-9]{32,}']
        proibidos = {'.env', 'secrets.toml', 'kaggle.json'}
        for arquivo in arquivos_do_projeto():
            self.assertNotIn(arquivo.name, proibidos, str(arquivo))
            if arquivo.suffix in {'.py', '.md', '.txt', '.json', '.ipynb', '.toml'}:
                conteudo = arquivo.read_text(encoding='utf-8', errors='replace')
                for padrao in padroes:
                    self.assertIsNone(re.search(padrao, conteudo), str(arquivo))


# [IA] Codex – Testes dos widgets.
class TestInterface(unittest.TestCase):
    def novo_app(self):
        st.cache_data.clear()
        app = AppTest.from_file(str(RAIZ / 'app.py'), default_timeout=60).run()
        self.assertEqual(len(app.exception), 0, str(app.exception))
        return app

    def test_duas_abas_e_todos_histogramas(self):
        app = self.novo_app()
        self.assertEqual(len(app.tabs), 2)
        self.assertEqual(len(app.get('image')), 12)
        self.assertEqual(app.metric[0].value, '13.397')
        self.assertTrue(any('Aguardando' in x.value for x in app.tabs[1].info))

    def test_selecao_zero_um_e_duas(self):
        app = self.novo_app()
        for selecao, imagens in [([], 0), (['minutes_played'], 1),
                                (['minutes_played', 'match_rating'], 3)]:
            app.multiselect(key='variaveis').set_value(selecao).run()
            self.assertEqual(len(app.exception), 0)
            self.assertEqual(len(app.get('image')), imagens)
            self.assertEqual(len(app.tabs), 2)

    def test_slider_filtra_e_restaura(self):
        app = self.novo_app()
        app.multiselect(key='variaveis').set_value(['minutes_played', 'match_rating']).run()
        app.slider(key='intervalo_minutes_played').set_value((30, 60)).run()
        esperado = carregar_dados().minutes_played.between(30, 60).sum()
        self.assertEqual(app.metric[1].value, f'{esperado:,}'.replace(',', '.'))
        self.assertEqual(len(app.get('image')), 3)
        app.slider(key='intervalo_minutes_played').set_value((1, 90)).run()
        self.assertEqual(app.metric[1].value, '13.397')
        self.assertEqual(len(app.exception), 0)

    def test_troca_variavel_e_recorte_vazio(self):
        app = self.novo_app()
        app.selectbox(key='variavel_filtro').set_value('market_value_eur_m').run()
        app.slider(key='intervalo_market_value_eur_m').set_value((100.01, 100.01)).run()
        self.assertEqual(app.metric[1].value, '0')
        self.assertEqual(len(app.get('image')), 0)
        self.assertEqual(len(app.tabs), 2)
        self.assertEqual(len(app.exception), 0)

    def test_slider_e_histograma_constante(self):
        app = self.novo_app()
        app.selectbox(key='variavel_filtro').set_value('goals').run()
        app.multiselect(key='variaveis').set_value(['goals']).run()
        app.slider(key='intervalo_goals').set_value((0, 0)).run()
        self.assertEqual(len(app.get('image')), 1)
        self.assertTrue(any('constante' in c.value for c in app.caption))
        self.assertEqual(len(app.exception), 0)

    def test_arquivo_ausente_nao_esconde_aba2(self):
        st.cache_data.clear()
        with patch('dados.carregar_dados', side_effect=FileNotFoundError('Arquivo ausente (teste)')):
            app = AppTest.from_file(str(RAIZ / 'app.py'), default_timeout=60).run()
        self.assertEqual(len(app.exception), 0)
        self.assertEqual(len(app.error), 1)
        self.assertEqual(len(app.tabs), 2)

    # [IA] Codex – Constantes e ausentes.
    def test_controle_constante_e_totalmente_ausente(self):
        for valor, imagens in [(45, 1), (float('nan'), 0)]:
            pequeno = carregar_dados().iloc[:4].copy()
            pequeno['minutes_played'] = valor
            st.cache_data.clear()
            app = AppTest.from_file(str(RAIZ / 'app.py'), default_timeout=60)
            app.session_state['variaveis'] = ['minutes_played']
            with patch('dados.carregar_dados', return_value=pequeno):
                app.run()
            self.assertEqual(len(app.exception), 0)
            self.assertEqual(len(app.slider), 0)
            self.assertEqual(len(app.get('image')), imagens)
            self.assertEqual(len(app.tabs), 2)

    def test_histograma_sem_valores(self):
        pequeno = carregar_dados().iloc[:4].copy()
        pequeno['age'] = float('nan')
        st.cache_data.clear()
        app = AppTest.from_file(str(RAIZ / 'app.py'), default_timeout=60)
        app.session_state['variaveis'] = ['age']
        with patch('dados.carregar_dados', return_value=pequeno):
            app.run()
        self.assertEqual(len(app.exception), 0)
        self.assertEqual(len(app.get('image')), 0)
        self.assertTrue(any('Sem valores disponíveis' in i.value for i in app.info))


# [IA] Codex – Executar testes.
if __name__ == '__main__':
    unittest.main()
