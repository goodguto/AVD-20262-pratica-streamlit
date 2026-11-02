# [IA] Codex – Testes dos indicadores escolhidos pelo aluno.
from pathlib import Path
import sys
import unittest

import pandas as pd
from streamlit.testing.v1 import AppTest

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))
from dados import carregar_dados
from indicadores import agrupar_jogadores, calcular_indicadores, filtrar_desempenho


# [IA] Codex – Conferir agregação e filtros sem alterar a base.
class TestIndicadores(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'player_name': ['A', 'A', 'A', 'B'],
            'nationality': ['Brasil', 'Brasil', 'Brasil', 'Chile'],
            'position': ['FW', 'FW', 'FW', 'MF'],
            'age': [20, 20, 20, 40],
            'goals': [1, 2, 1, 3],
            'assists': [0, 1, 0, 2],
        })

    def test_idade_nao_e_ponderada_por_participacoes(self):
        valores = calcular_indicadores(self.df)
        self.assertEqual(valores, {'gols': 7, 'assistencias': 3, 'idade_media': 30.0})
        self.assertNotEqual(valores['idade_media'], self.df.age.mean())

    def test_um_registro_por_jogador(self):
        jogadores = agrupar_jogadores(self.df).set_index('player_name')
        self.assertEqual(len(jogadores), 2)
        self.assertEqual(jogadores.loc['A', 'goals'], 4)
        self.assertEqual(jogadores.loc['A', 'assists'], 1)

    def test_filtros_combinados_e_limites_inclusivos(self):
        antes = self.df.copy(deep=True)
        resultado = filtrar_desempenho(self.df, 'Brasil', 'FW', (20, 20))
        self.assertEqual(calcular_indicadores(resultado), {'gols': 4, 'assistencias': 1, 'idade_media': 20.0})
        resultado.loc[:, 'age'] = 0
        pd.testing.assert_frame_equal(self.df, antes)

    def test_recorte_vazio(self):
        vazio = filtrar_desempenho(self.df, 'Brasil', 'MF')
        self.assertTrue(vazio.empty)
        self.assertEqual(calcular_indicadores(vazio), {'gols': None, 'assistencias': None, 'idade_media': None})

    def test_todos_ausentes_nao_viram_zero(self):
        self.df['goals'] = float('nan')
        self.df['assists'] = float('nan')
        self.df['age'] = float('nan')
        self.assertEqual(calcular_indicadores(self.df), {'gols': None, 'assistencias': None, 'idade_media': None})

    def test_intervalo_invertido(self):
        with self.assertRaises(ValueError):
            filtrar_desempenho(self.df, idades=(30, 20))


# [IA] Codex – Conferir os cartões e gráficos pelo app real.
class TestDashboard2(unittest.TestCase):
    def iniciar(self):
        app = AppTest.from_file(str(RAIZ / 'app.py'), default_timeout=60).run()
        self.assertFalse(app.exception, app.exception)
        return app

    def metrica(self, app, nome):
        return next(m.value for m in app.metric if m.label == nome)

    def test_tres_indicadores_e_tres_graficos(self):
        app = self.iniciar()
        valores = calcular_indicadores(carregar_dados())
        self.assertEqual(self.metrica(app, 'Gols'), f"{valores['gols']:,}".replace(',', '.'))
        self.assertEqual(self.metrica(app, 'Assistências'), f"{valores['assistencias']:,}".replace(',', '.'))
        self.assertEqual(len(app.get('vega_lite_chart')), 3)
        self.assertEqual(len(app.tabs), 2)

    def test_filtros_atualizam_indicadores_e_populacao_dos_graficos(self):
        app = self.iniciar()
        app.selectbox(key='d2_pais').set_value('Morocco').run()
        app.selectbox(key='d2_posicao').set_value('RB').run()
        app.slider(key='d2_idade').set_value((20, 30)).run()
        self.assertFalse(app.exception, app.exception)
        esperado = filtrar_desempenho(carregar_dados(), 'Morocco', 'RB', (20, 30))
        metricas = calcular_indicadores(esperado)
        self.assertEqual(self.metrica(app, 'Gols'), f"{metricas['gols']:,}".replace(',', '.'))
        pd.testing.assert_frame_equal(app.dataframe[-1].value, agrupar_jogadores(esperado))
        self.assertEqual(len(app.get('vega_lite_chart')), 3)

    def test_vazio_na_interface(self):
        app = self.iniciar()
        app.selectbox(key='d2_pais').set_value('Morocco').run()
        app.slider(key='d2_idade').set_value((17, 17)).run()
        self.assertFalse(app.exception, app.exception)
        self.assertEqual(self.metrica(app, 'Gols'), '—')
        self.assertEqual(self.metrica(app, 'Idade média por jogador'), '—')
        self.assertEqual(len(app.get('vega_lite_chart')), 0)


# [IA] Codex – Executar testes.
if __name__ == '__main__':
    unittest.main()
