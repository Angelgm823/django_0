# ────────────────────────────────
# 0. Imports y utilidades
# ────────────────────────────────
import random
import itertools
from datetime import date, timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model

from libreria.models import (
    Autor, Genero, Libros, DetallesLibro,
    Critica, Prestamo, Recomendaciones
)

User = get_user_model()

# ────────────────────────────────
# 1. Usuarios (20)
# ────────────────────────────────
users = [
    User(username=f"user{i}", email=f"user{i}@demo.com")
    for i in range(1, 21)
]
# Hash de password seguro:
for u in users:
    u.set_password("pass1234")
User.objects.bulk_create(users)

users = list(User.objects.all())   # recargamos con IDs

# ────────────────────────────────
# 2. Autores (20)
# ────────────────────────────────
autores = [
    Autor(nombre=f"Autor {i}", fecha_nacimiento=date(1950+i, 1, 1))
    for i in range(1, 21)
]
Autor.objects.bulk_create(autores)
autores = list(Autor.objects.all())

# ────────────────────────────────
# 3. Géneros (20)
# ────────────────────────────────
generos = [
    Genero(nombre=gn) for gn in [
        "Ciencia Ficción", "Distopía",
        "Aventura", "Romance", "Misterio", "Histórico",
        "Poesía", "Fantástico", "Biografía", "Ensayo",
        "Horror", "Thriller", "Policíaco", "Humor",
        "Infantil", "Juvenil", "Filosofía", "Autoayuda"
    ]
]
Genero.objects.bulk_create(generos)
generos = list(Genero.objects.all())

# ────────────────────────────────
# 4. Libros (20)
# ────────────────────────────────
libros = []
for i in range(1, 21):
    libros.append(
        Libros(
            titulo=f"Libro {i}",
            fecha_publicacion=date(2000+i, 6, 1),
            autor=random.choice(autores),
            paginas=random.randint(150, 600),
            isbn=f"ISBN-{1000+i}"
        )
    )
Libros.objects.bulk_create(libros)
libros = list(Libros.objects.all())

# Many-to-Many (asigna 2 géneros aleatorios a cada libro)
for libro in libros:
    libro.generos.add(*random.sample(generos, 2))

# ────────────────────────────────
# 5. libroDetail (20)  – uno por libro
# ────────────────────────────────
detalles = []
for libro in libros:
    detalles.append(
        DetallesLibro(
            libro=libro,
            resumen=f"Resumen de {libro.titulo}",
            portada_url=f"https://picsum.photos/seed/{libro.id}/200/300",
            lenguaje=random.choice(["Español", "Inglés", "Francés"])
        )
    )
DetallesLibro.objects.bulk_create(detalles)

# ────────────────────────────────
# 6. Reviews (20)
# ────────────────────────────────
criticas = []
for i in range(20):
    criticas.append(
        Critica(
            usuario=random.choice(users),
            libro=random.choice(libros),
            calificacion=random.randint(1, 5),
            texto="Excelente lectura" if i % 2 == 0 else "Interesante pero mejorable"
        )
    )
Critica.objects.bulk_create(criticas)

# ────────────────────────────────
# 7. Loans (20)  – la mitad devueltos
# ────────────────────────────────
prestamos = []
today = timezone.now()
for i in range(20):
    loan_date = today - timedelta(days=random.randint(1, 60))
    returned = i % 2 == 0
    prestamos.append(
        Prestamo(
            usuario=random.choice(users),
            libro=random.choice(libros),
            fecha_prestamo=loan_date,
            estado=returned,
            fecha_ingreso=loan_date + timedelta(days=15) if returned else None
        )
    )
Prestamo.objects.bulk_create(prestamos)

# ────────────────────────────────
# 8. Recommendations (20)
# ────────────────────────────────
recs = []
libro_cycle = itertools.cycle(libros)
for i in range(20):
    recs.append(
        Recomendaciones(
            usuario=random.choice(users),
            libro=next(libro_cycle),
            nota="¡Tienes que leerlo!"
        )
    )
Recomendaciones.objects.bulk_create(recs)

print("✅ ¡20 registros creados en cada tabla!")