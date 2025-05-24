const carouselSidebar = document.getElementById('carouselExampleCaptions');
const captionTitleSidebar = document.getElementById('sidebar-caption-title');
const captionTextSidebar = document.getElementById('sidebar-caption-text');

carouselSidebar.addEventListener('slide.bs.carousel', event => {
    const activeItem = event.relatedTarget;
    const captionParts = activeItem.getAttribute('data-caption').split('||'); // Supondo título||texto
    captionTitleSidebar.textContent = captionParts[0] || '';
    captionTextSidebar.textContent = captionParts[1] || '';
});

// Atualizar a legenda inicial da barra lateral
const firstCaptionSidebar = carouselSidebar.querySelector('.carousel-item.active').getAttribute('data-caption').split('||');
captionTitleSidebar.textContent = firstCaptionSidebar[0] || '';
captionTextSidebar.textContent = firstCaptionSidebar[1] || '';