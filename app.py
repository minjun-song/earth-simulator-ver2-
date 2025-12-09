import pathlib
import streamlit as st
from streamlit.components.v1 import html

FILE_NAME = "earth_heat_balance_simulator.html"


def load_html(file_name: str) -> str:
    """Load HTML content from a file located in the current directory."""
    path = pathlib.Path(__file__).resolve().parent / file_name
    return path.read_text(encoding="utf-8")


def main() -> None:
    st.set_page_config(page_title="지구 열수지 시뮬레이터", layout="wide")
    st.title("지구 열수지 시뮬레이터")
    st.markdown("알베도 조절, 퀴즈, 지구온난화 모드를 지원하는 시뮬레이터를 아래에서 확인하세요.")

    html_content = load_html(FILE_NAME)
    html(html_content, height=800, scrolling=True)


if __name__ == "__main__":
    main()
