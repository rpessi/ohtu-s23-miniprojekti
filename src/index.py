from console_io import ConsoleIO
from app import App
from database_connection import get_db_connection
from services.reference_service import ReferenceService
from repositories.reference_repository import ReferenceRepository
from file_io import FileIO
from bibtex_writer import BibTexWriter


def main():
    console_io = ConsoleIO()
    connection = get_db_connection()
    reference_repository = ReferenceRepository(connection)
    reference_service = ReferenceService(reference_repository)
    bibtex_writer = BibTexWriter(FileIO())

    app = App(console_io, reference_service, bibtex_writer)

    app.run()


if __name__ == "__main__":
    main()
