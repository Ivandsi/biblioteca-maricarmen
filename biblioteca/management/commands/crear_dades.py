from django.core.management.base import BaseCommand
import random
from faker import Faker
from biblioteca.models import Llibre, Llengua, Pais, Categoria
    
class Command(BaseCommand):
    help = "Genera 40 llibres amb Faker (10 per idioma: Català, Castellà, Anglès, Francès)"

    def handle(self, *args, **kwargs):
        # Configurar Faker per a diferents idiomes
        faker_ca = Faker("es_CA")
        faker_es = Faker("es_ES")
        faker_en = Faker("en_US")
        faker_fr = Faker("fr_FR")

        IDIOMES = {
            "Català": faker_ca,
            "Castellà": faker_es,
            "Anglès": faker_en,
            "Francès": faker_fr,
        }

        def crear_llibre(idioma_nom, faker_instance):
            # Obtenir o crear Llengua
            llengua, _ = Llengua.objects.get_or_create(nom=idioma_nom)


            # Crear el llibre
            llibre = Llibre.objects.create(
                titol=faker_instance.sentence(nb_words=4),
                autor=faker_instance.name(),
                ISBN=faker_instance.isbn13(),
                editorial=faker_instance.company(),
                llengua=llengua,
            )

            self.stdout.write(self.style.SUCCESS(f"Llibre creat: {llibre.titol} ({idioma_nom})"))

        # Generar 40 llibres (10 per idioma)
        for idioma, faker_instance in IDIOMES.items():
            for _ in range(10):
                crear_llibre(idioma, faker_instance)

        self.stdout.write(self.style.SUCCESS("✅ Seeder completat! 40 llibres afegits."))