import streamlit as st
import pandas as pd


def read_csv_data(csv_file):
    df = pd.read_csv(csv_file)
    return df

def main():
    st.set_page_config(layout="wide")
    st.title("가계부 애플리케이션")

    # 전체 레이아웃을 좌우로 나누기
    left_column, right_column = st.columns(2)

    # 사용자의 입력 정보 영역 (좌측)
    with left_column:
        st.subheader("거래 입력")
        date = st.text_input("거래일자")

        pos = st.selectbox("수익 / 지출", ["수익", "지출"])

        category = st.selectbox("카테고리", ["식비", "교통", "주거", "의류", "기타"])

        amount = st.text_input("금액")
        memo = st.text_input("메모")

        # 입력된 거래 정보 처리
        if st.button("저장"):
            # 입력된 정보를 이용하여 데이터 처리 로직 추가
            pass

    # CSV 데이터를 읽고 출력하는 영역 (우측)
    with right_column:
        csv_file_path = "household.csv"  # 읽고자 하는 CSV 파일의 경로
        df = pd.read_csv(csv_file_path, index_col=0)  # index_col=0
        # df = read_csv_data(csv_file_path)
        st.subheader("거래 내역")
        st.dataframe(df, height=400, width=1200)  # 표의 높이를 400으로 설정


if __name__ == "__main__":
    main()
