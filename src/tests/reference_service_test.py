import unittest
from entities.book_reference import BookReference
from entities.article_reference import ArticleReference
from services.reference_service import ReferenceService


class FakeReferenceRepository:
    def __init__(self):
        self.references = []

    def get_all(self):
        return self.references

    def create_book(self, book):
        self.references.append(book)
        return book

    def create_article(self, article):
        self.references.append(article)
        return article

    def delete_all(self):
        self.references = []

    def get_book_by_ref_key(self, ref_key):
        return True

    def delete_book_by_ref_key(self, ref_key):
        return True


class TestReferenceService(unittest.TestCase):
    def setUp(self):
        self.reference_service = ReferenceService(FakeReferenceRepository())
        self.test_book = {}
        self.test_book["type"] = "book"
        self.test_book["ref_key"] = "KEY"
        self.test_book["author"] = "test_author"
        self.test_book["title"] = "test_title"
        self.test_book["year"] = "2023"
        self.test_book["publisher"] = "OTA"

        self.test_article = {"type": "article",
                             "ref_key": "abc",
                             "author": "joku",
                             "title": "jotain",
                             "journal": "aku-ankka",
                             "year": 2023,
                             "volume": 2,
                             "pages": "1-3"}

    def test_create_reference_book(self):
        self.reference_service.create_reference(self.test_book)
        reference_list = self.reference_service.get_all()
        expected_book = reference_list[0]

        self.assertEqual(len(reference_list), 1)
        self.assertEqual(expected_book.ref_key, self.test_book["ref_key"])
        self.assertEqual(expected_book.author, self.test_book["author"])
        self.assertEqual(expected_book.title, self.test_book["title"])
        self.assertEqual(expected_book.year, self.test_book["year"])
        self.assertEqual(expected_book.publisher, self.test_book["publisher"])

    def test_create_reference_article(self):
        self.reference_service.create_reference(self.test_article)
        reference_list = self.reference_service.get_all()
        expected_article = reference_list[0]

        self.assertEqual(len(reference_list), 1)
        self.assertEqual(expected_article.ref_key,
                         self.test_article["ref_key"])
        self.assertEqual(expected_article.author, self.test_article["author"])
        self.assertEqual(expected_article.title, self.test_article["title"])
        self.assertEqual(expected_article.journal,
                         self.test_article["journal"])
        self.assertEqual(expected_article.year, self.test_article["year"])
        self.assertEqual(expected_article.volume, self.test_article["volume"])
        self.assertEqual(expected_article.pages, self.test_article["pages"])

    def test_get_fields_of_reference_type_book(self):
        fields = self.reference_service.get_fields_of_reference_type("book")
        self.assertEqual(fields, ["ref_key", "author",
                         "title", "year", "publisher"])

    def test_get_fields_of_reference_type_not_found_returns_empty(self):
        fields = self.reference_service.get_fields_of_reference_type(
            "notfound")
        self.assertEqual(len(fields), 0)

    def test_get_book_by_ref_key_calls_repository(self):
        self.assertTrue(self.reference_service.get_book_by_ref_key("1"))

    def test_delete_book_by_ref_key_calls_repository(self):
        self.assertTrue(self.reference_service.delete_book_by_ref_key("1"))

    def test_ref_key_taken_returns_false_if_not_taken(self):
        taken = self.reference_service.ref_key_taken("1")

        self.assertFalse(taken)

    def test_ref_key_taken_returns_true_if_taken(self):
        self.reference_service.create_reference(self.test_book)
        taken = self.reference_service.ref_key_taken("KEY")

        self.assertTrue(taken)
