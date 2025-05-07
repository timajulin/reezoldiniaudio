import unittest
from app import app, db, Product
import os

class TestReezoldiniAudio(unittest.TestCase):
    def setUp(self):
        """Настройка тестового окружения"""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.client = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()
        
        # Добавляем тестовые данные
        test_product = Product(
            name='Test Headphones',
            category='headphones',
            description='Test description',
            price=99999.00,
            image_url='static/images/headphones-1.jpg'
        )
        db.session.add(test_product)
        db.session.commit()

    def tearDown(self):
        """Очистка после тестов"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        if os.path.exists('test.db'):
            os.remove('test.db')

    def test_home_page(self):
        """Тест главной страницы"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'РИЗОЛДИНИ аудио', response.data)
        self.assertIn(b'Unbound', response.data)
        self.assertIn(b'sound', response.data)
        self.assertIn(b'experience', response.data)

    def test_about_page(self):
        """Тест страницы 'О нас'"""
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'О нас', response.data)

    def test_contact_page(self):
        """Тест страницы контактов"""
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Свяжитесь с нами', response.data)

    def test_category_filter(self):
        """Тест фильтрации по категории"""
        response = self.client.get('/products?category=headphones')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Headphones', response.data)
        # Проверяем, что отображаются только наушники
        self.assertNotIn(b'REEZOLDINI Reference Amp', response.data)

    def test_product_display(self):
        """Тест отображения товара"""
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Headphones', response.data)
        self.assertIn(b'Test description', response.data)
        self.assertIn(b'99999.00', response.data)
        self.assertIn(b'headphones-1.jpg', response.data)

if __name__ == '__main__':
    unittest.main() 