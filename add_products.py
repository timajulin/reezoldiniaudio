from app import app, db, Product

# Создаем список продуктов
products = [
    {
        'name': 'REEZOLDINI Jericho M',
        'category': 'speakers',
        'description': '2,5-полосная акустика с тремя активными драйверами и четырьмя пассивными радиаторами Scan-Speak revelator.',
        'price': 449999.00,
        'image_url': 'static/images/Reezoldini-SAV-JM-12W960.jpg'
    },
    {
        'name': 'REEZOLDINI  Cimema 7F',
        'category': 'speakers',
        'description': '2,5-полосные акустические системы с тремя активными драйверами и четырьмя пассивными радиаторами Scan-Speak revelator.',
        'price': 299999.00,
        'image_url': 'static/images/Reezoldini-Cinema-7F-01.jpg'
    },
    {
        'name': 'REEZOLDINI Reference Amp',
        'category': 'amplifiers',
        'description': 'Высококлассный интегральный усилитель класса AB мощностью 2x200W с балансными входами и высококачественным ЦАП.',
        'price': 399999.00,
        'image_url': 'static/images/amp-1.jpg'
    },
    {
        'name': 'REEZOLDINI Signature Headphones',
        'category': 'headphones',
        'description': 'Премиальные наушники закрытого типа с 50мм динамическими драйверами и частотным диапазоном 5Hz-45kHz.',
        'price': 149999.00,
        'image_url': 'static/images/headphones-1.jpg'
    }
]

def add_products():
    with app.app_context():
        # Очищаем таблицу продуктов
        Product.query.delete()
        
        # Добавляем новые продукты
        for product_data in products:
            product = Product(**product_data)
            db.session.add(product)
        
        # Сохраняем изменения
        db.session.commit()
        print("Продукты успешно добавлены в базу данных!")

if __name__ == '__main__':
    add_products()
