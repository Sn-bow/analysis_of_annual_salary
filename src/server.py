import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# Relationship between annual salary and college major
df = pd.read_csv("./static/data/major_early_data.csv", thousands = ',')


# Relationship between annual salary and college major : all data
@app.route('/r_sal_maj')
def get_all_data():
    r_sal_maj = df.to_dict(orient="records")
    return jsonify(r_sal_maj)




# column data
## Mid-Career Pay column data & ascending
@app.route("/r_sal_maj/mid_career_pay_all")
def get_mid_car_pay_data():
    mid_career_pay_dic = df[["Mid-Career Pay", "id"]].to_dict(orient="records")
    return jsonify(mid_career_pay_dic)

@app.route("/r_sal_maj/mid_career_pay_all/ascending")
def get_mid_car_pay_ascending_data():
    mid_career_pay_dic = df[["Mid-Career Pay", "id"]].sort_values("Mid-Career Pay").to_dict(orient="records")
    return jsonify(mid_career_pay_dic)

## Early Career Pay column data
@app.route("/r_sal_maj/ear_career_pay_all")
def get_ear_car_pay_data():
    ear_career_pay = df[["Early Career Pay", "id"]].to_dict(orient="records")
    return jsonify(ear_career_pay)

@app.route("/r_sal_maj/ear_career_pay_all/ascending")
def get_ear_car_pay_ascending_data():
    ear_career_pay = df[["Early Career Pay", "id"]].sort_values("Early Career Pay").to_dict(orient="records")
    return jsonify(ear_career_pay)

## Major column data
@app.route("/r_sal_maj/major_all")
def get_major_data():
    major = df[["Major", "id"]].to_dict(orient="records")
    return jsonify(major)

## High Meaning % column data
@app.route("/r_sal_maj/high_meaning_all")
def get_high_meaning_data():
    high_meaning = df[["High Meaning %", "id"]].to_dict(orient="records")
    return jsonify(high_meaning)

@app.route("/r_sal_maj/high_meaning_all/ascending")
def get_high_meaning_ascending_data():
    high_meaning = df[["High Meaning %", "id"]].sort_values("High Meaning %").to_dict(orient="records")
    return jsonify(high_meaning)




# ascending & deascending get

# Mid-Career Pay json data
## Mid-Career Pay json data : ascending order
@app.route("/r_sal_maj/mid_career_pay_ascending")   # page 1
def get_mid_career_pay_ascending():
    df["Mid-Career Pay"] = pd.to_numeric(df["Mid-Career Pay"])
    mid_career_pay_ascending_df = df.sort_values(by="Mid-Career Pay")
    mid_career_pay_ascending_dic = mid_career_pay_ascending_df.to_dict(orient="records")
    return jsonify(mid_career_pay_ascending_dic[:10])

@app.route("/r_sal_maj/ear_career_pay_ascending/<int:page>")   # page choice
def get_mid_career_pay_ascending_page(page):
    df["Mid-Career Pay"] = pd.to_numeric(df["Mid-Career Pay"])
    mid_career_pay_ascending_df = df.sort_values(by="Mid-Career Pay")
    mid_career_pay_ascending_dic = mid_career_pay_ascending_df.to_dict(orient="records")
    next_page = page * 10
    if not mid_career_pay_ascending_dic[next_page - 10:next_page]:
        return jsonify(error="data is empty")
    else:
        return jsonify(mid_career_pay_ascending_dic[next_page - 10:next_page])

## Mid-Career Pay json data : deascending order
@app.route("/r_sal_maj/mid_career_pay_ascending")   # page 1
def get_mid_career_pay_deascending():
    df["Mid-Career Pay"] = pd.to_numeric(df["Mid-Career Pay"])
    mid_career_pay_deascending_df = df.sort_values(by="Mid-Career Pay")
    mid_career_pay_deascending_dic = mid_career_pay_deascending_df.to_dict(orient="records")
    return jsonify(mid_career_pay_deascending_dic[:10])

@app.route("/r_sal_maj/ear_career_pay_ascending/<int:page>")   # page choice
def get_mid_career_pay_deascending_page(page):
    df["Mid-Career Pay"] = pd.to_numeric(df["Mid-Career Pay"])
    mid_career_pay_deascending_df = df.sort_values(by="Mid-Career Pay")
    mid_career_pay_deascending_dic = mid_career_pay_deascending_df.to_dict(orient="records")
    next_page = page * 10
    if not mid_career_pay_deascending_dic[next_page - 10:next_page]:
        return jsonify(error="data is empty")
    else:
        return jsonify(mid_career_pay_deascending_dic[next_page - 10:next_page])


# early career pay josn data
## early career pay josn data : ascending order 
@app.route("/r_sal_maj/ear_career_pay_ascending")   # page 1
def get_ear_career_pay_ascending():
    df["Early Career Pay"] = pd.to_numeric(df["Early Career Pay"])
    ear_career_pay_ascending_df = df.sort_values(by="Early Career Pay")
    ear_career_pay_ascending_dic = ear_career_pay_ascending_df.to_dict(orient="records")
    return jsonify(ear_career_pay_ascending_dic[:10])

@app.route("/r_sal_maj/ear_career_pay_ascending/<int:page>")   # page choice
def get_ear_career_pay_ascending_page(page):
    df["Early Career Pay"] = pd.to_numeric(df["Early Career Pay"])
    ear_career_pay_ascending_df = df.sort_values(by="Early Career Pay")
    ear_career_pay_ascending_dic = ear_career_pay_ascending_df.to_dict(orient="records")
    next_page = page * 10
    if not ear_career_pay_ascending_dic[next_page - 10:next_page]:
        return jsonify(error="data is empty")
    else:
        return jsonify(ear_career_pay_ascending_dic[next_page - 10:next_page])

## early career pay josn data : ascending order 
@app.route("/r_sal_maj/ear_career_pay_deascending")   # page 1
def get_ear_career_pay_deascending():
    df["Early Career Pay"] = pd.to_numeric(df["Early Career Pay"])
    ear_career_pay_deascending_df = df.sort_values(by="Early Career Pay")
    ear_career_pay_deascending_dic = ear_career_pay_deascending_df.to_dict(orient="records")
    return jsonify(ear_career_pay_deascending_dic[:10])

@app.route("/r_sal_maj/ear_career_pay_deascending/<int:page>")   # page choice
def get_ear_career_pay_deascending_page(page):
    df["Early Career Pay"] = pd.to_numeric(df["Early Career Pay"])
    ear_career_pay_deascending_df = df.sort_values(by="Early Career Pay")
    ear_career_pay_deascending_dic = ear_career_pay_deascending_df.to_dict(orient="records")
    next_page = page * 10
    if not ear_career_pay_deascending_dic[next_page - 10:next_page]:
        return jsonify(error="data is empty")
    else:
        return jsonify(ear_career_pay_deascending_dic[next_page - 10:next_page])



# high-meaning sorted json data
## high-meaning sorted json data : ascending order
@app.route("/r_sal_maj/high_meaning_ascending") # page 1
def get_high_meaning_ascending():
    high_meaning_ascending_df = df.sort_values(by="High Meaning %")
    high_meaning_ascending_dic = high_meaning_ascending_df.to_dict(orient="records")
    return jsonify(high_meaning_ascending_dic[:10])

@app.route("/r_sal_maj/high_meaning_ascending/<int:page>") # choice page <int:page>
def get_high_meaning_ascending_page(page):
    high_meaning_ascending_df = df.sort_values(by="High Meaning %")
    high_meaning_ascending_dic = high_meaning_ascending_df.to_dict(orient="records")
    next_page = page * 10
    if not high_meaning_ascending_dic[next_page - 10:next_page]:
        return jsonify(error="data is empty")
    else:
        return jsonify(high_meaning_ascending_dic[next_page - 10:next_page])


## high-meaning sorted json data : descending order
@app.route("/r_sal_maj/high_meaning_descending")
def get_high_meaning_descending():
    high_meaning_descending_df = df.sort_values(by="High Meaning %",ascending=False)
    high_meaning_descending_dic = high_meaning_descending_df.to_dict(orient="records")
    return jsonify(high_meaning_descending_dic[:10])


@app.route("/r_sal_maj/high_meaning_descending/<int:page>")
def get_high_meaning_descending_page(page):
    high_meaning_descending_df = df.sort_values(by="High Meaning %",ascending=False)
    high_meaning_descending_dic = high_meaning_descending_df.to_dict(orient="records")
    next_page = page * 10
    if not high_meaning_descending_dic[next_page - 10:next_page]:
        return jsonify(error="data is empty")
    else:
        return jsonify(high_meaning_descending_dic[next_page - 10:next_page])






if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0", debug=True)




