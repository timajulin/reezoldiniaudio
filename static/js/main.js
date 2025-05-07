// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Form validation
const contactForm = document.querySelector('form');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        const nameInput = document.getElementById('name');
        const emailInput = document.getElementById('email');
        const messageInput = document.getElementById('message');
        
        let isValid = true;
        
        if (!nameInput.value.trim()) {
            isValid = false;
            nameInput.classList.add('is-invalid');
        } else {
            nameInput.classList.remove('is-invalid');
        }
        
        if (!emailInput.value.trim() || !emailInput.value.includes('@')) {
            isValid = false;
            emailInput.classList.add('is-invalid');
        } else {
            emailInput.classList.remove('is-invalid');
        }
        
        if (!messageInput.value.trim()) {
            isValid = false;
            messageInput.classList.add('is-invalid');
        } else {
            messageInput.classList.remove('is-invalid');
        }
        
        if (!isValid) {
            e.preventDefault();
        }
    });
}

// Product image gallery
document.querySelectorAll('.product-gallery-thumb').forEach(thumb => {
    thumb.addEventListener('click', function() {
        const mainImage = this.closest('.product-gallery').querySelector('.product-gallery-main');
        mainImage.src = this.src;
    });
});

document.addEventListener('DOMContentLoaded', function() {
    // Header scroll effect
    const header = document.querySelector('header');
    const scrollThreshold = 100;

    function handleScroll() {
        if (window.scrollY > scrollThreshold) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }

    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Check initial scroll position

    // Light effect for glass containers
    const lightEffect = document.createElement('div');
    lightEffect.className = 'light-effect';
    document.body.appendChild(lightEffect);

    function updateLightEffect(e) {
        const mouseX = e.clientX;
        const mouseY = e.clientY;

        lightEffect.style.opacity = '1';
        lightEffect.style.transform = `translate(${mouseX - 150}px, ${mouseY - 150}px)`;

        document.querySelectorAll('.glass-container').forEach(container => {
            const rect = container.getBoundingClientRect();
            const x = ((mouseX - rect.left) / container.offsetWidth) * 100;
            const y = ((mouseY - rect.top) / container.offsetHeight) * 100;
            
            container.style.setProperty('--mouse-x', `${x}%`);
            container.style.setProperty('--mouse-y', `${y}%`);
        });
    }

    function hideLightEffect() {
        lightEffect.style.opacity = '0';
    }

    document.addEventListener('mousemove', updateLightEffect);
    document.addEventListener('mouseleave', hideLightEffect);
});
