from django.core.management.base import BaseCommand
import random
from faker import Faker
from biblioteca.models import *
    
class Command(BaseCommand):
    help = "Populates the database with sample data"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Crear o recuperar las lenguas
        llengues = {
            "Català": Llengua.objects.get_or_create(nom="Català")[0],
            "Castellano": Llengua.objects.get_or_create(nom="Castellano")[0],
            "English": Llengua.objects.get_or_create(nom="English")[0],
            "Français": Llengua.objects.get_or_create(nom="Français")[0],
        }

        # Crear libros (10 por lengua)
        for idioma, llengua in llengues.items():
            for _ in range(10):
                llibre = Llibre.objects.create(
                    titol=fake.sentence(nb_words=4),
                    titol_original=fake.sentence(nb_words=4),
                    autor=fake.name(),
                    CDU=fake.bothify(text="###.##"),
                    signatura=fake.bothify(text="SIG###"),
                    data_edicio=fake.date_between(start_date="-50y", end_date="today"),
                    resum=fake.text(),
                    anotacions=fake.text(),
                    mides=f"{random.randint(10, 30)}x{random.randint(10, 30)} cm",
                    ISBN=fake.isbn13(),
                    editorial=fake.company(),
                    colleccio=fake.word(),
                    lloc=fake.city(),
                    pais=Pais.objects.order_by("?").first(),  # Elige un país aleatorio si hay datos
                    llengua=llengua,
                    numero=random.randint(1, 20),
                    volums=random.randint(1, 5),
                    pagines=random.randint(50, 1000),
                    info_url=fake.url(),
                    preview_url=fake.url(),
                    thumbnail_url=fake.image_url()
                )

                # Crear 2 ejemplares por libro
                for _ in range(2):
                    Exemplar.objects.create(
                        cataleg=llibre,
                        registre=fake.uuid4()[:8],
                        exclos_prestec=random.choice([True, False]),
                        baixa=random.choice([True, False])
                    )

        # Crear 50 usuarios
        for _ in range(50):
            Usuari.objects.create(
                username=fake.user_name(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                centre=Centre.objects.order_by("?").first(),  # Elige un centro aleatorio si hay datos
                cicle=Cicle.objects.order_by("?").first(),  # Elige un ciclo aleatorio si hay datos
                imatge=None,  # Puedes cambiar esto si necesitas subir imágenes
                auth_token=fake.uuid4()[:32]
            )

        self.stdout.write(self.style.SUCCESS("✅ Base de datos poblada con libros, ejemplares y usuarios."))