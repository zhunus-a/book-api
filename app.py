from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {
        "id": 1,
        "title": "Абай жолы",
        "author": "Мұхтар Әуезов",
        "year": 1942
    },
    {
        "id": 2,
        "title": "Ақбілек",
        "author": "Жүсіпбек Аймауытов",
        "year": 1927
    },
    {
        "id": 3,
        "title": "Қамар сұлу",
        "author": "Сұлтанмахмұт Торайғыров",
        "year": 1914
    },
    {
        "id": 4,
        "title": "Бақытсыз Жамал",
        "author": "Міржақып Дулатұлы",
        "year": 1910
    },
    {
        "id": 5,
        "title": "Қан мен тер",
        "author": "Әбдіжәміл Нұрпейісов",
        "year": 1961
    },
    {
        "id": 6,
        "title": "Көшпенділер",
        "author": "Ілияс Есенберлин",
        "year": 1969
    },
    {
        "id": 7,
        "title": "Алмас қылыш",
        "author": "Ілияс Есенберлин",
        "year": 1971
    },
    {
        "id": 8,
        "title": "Жанталас",
        "author": "Ілияс Есенберлин",
        "year": 1973
    },
    {
        "id": 9,
        "title": "Қаһар",
        "author": "Ілияс Есенберлин",
        "year": 1969
    },
    {
        "id": 10,
        "title": "Ұлпан",
        "author": "Ғабит Мүсірепов",
        "year": 1974
    },
    {
        "id": 11,
        "title": "Оянған өлке",
        "author": "Ғабит Мүсірепов",
        "year": 1953
    },
    {
        "id": 12,
        "title": "Қазақ солдаты",
        "author": "Ғабит Мүсірепов",
        "year": 1949
    },
    {
        "id": 13,
        "title": "Менің атым Қожа",
        "author": "Бердібек Соқпақбаев",
        "year": 1957
    },
    {
        "id": 14,
        "title": "Балалық шаққа саяхат",
        "author": "Бердібек Соқпақбаев",
        "year": 1960
    },
    {
        "id": 15,
        "title": "Жусан иісі",
        "author": "Сайын Мұратбеков",
        "year": 1970
    },
    {
        "id": 16,
        "title": "Махаббат, қызық мол жылдар",
        "author": "Әзілхан Нұршайықов",
        "year": 1970
    },
    {
        "id": 17,
        "title": "Шұғаның белгісі",
        "author": "Бейімбет Майлин",
        "year": 1915
    },
    {
        "id": 18,
        "title": "Раушан-коммунист",
        "author": "Бейімбет Майлин",
        "year": 1929
    },
    {
        "id": 19,
        "title": "Қилы заман",
        "author": "Мұхтар Әуезов",
        "year": 1928
    },
    {
        "id": 20,
        "title": "Қараш-Қараш оқиғасы",
        "author": "Мұхтар Әуезов",
        "year": 1927
    },
    {
        "id": 21,
        "title": "Еңлік-Кебек",
        "author": "Мұхтар Әуезов",
        "year": 1917
    },
    {
        "id": 22,
        "title": "Көксерек",
        "author": "Мұхтар Әуезов",
        "year": 1929
    },
    {
        "id": 23,
        "title": "Ақан сері – Ақтоқты",
        "author": "Ғабит Мүсірепов",
        "year": 1942
    },
    {
        "id": 24,
        "title": "Аласапыран",
        "author": "Мұхтар Мағауин",
        "year": 1981
    },
    {
        "id": 25,
        "title": "Тар жол, тайғақ кешу",
        "author": "Сәкен Сейфуллин",
        "year": 1927
    },
    {
        "id": 26,
        "title": "Қартқожа",
        "author": "Жүсіпбек Аймауытов",
        "year": 1926
    },
    {
        "id": 27,
        "title": "Көкшетау",
        "author": "Сәкен Сейфуллин",
        "year": 1929
    },
    {
        "id": 28,
        "title": "Үш бақытым",
        "author": "Мұқағали Мақатаев",
        "year": 1960
    },
    {
        "id": 29,
        "title": "Өмірзая",
        "author": "Болат Мұқай",
        "year": 1991
    },
    {
        "id": 30,
        "title": "Дарабоз",
        "author": "Қабдеш Жұмаділов",
        "year": 1994
    }
]


@app.route("/")
def home():
    return "Welcome to the Book API"


@app.route("/healthz")
def health():
    return "OK", 200


@app.route("/books")
def get_books():
    return jsonify(books)


@app.route("/books/<int:book_id>")
def get_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return jsonify(book)

    return jsonify({"error": "Book not found"}), 404


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 8080))

    app.run(host="0.0.0.0", port=port)