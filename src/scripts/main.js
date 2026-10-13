// Comportamientos del origen en JavaScript nativo. Un único archivo: las páginas son entradas separadas y
// Vite sólo genera un script por página si no hay trozos compartidos (htmlAutonomo, file://).
// Secciones: foco atrapado, cabecera, página, revelado, slider, diálogo y formularios.

// ---- focus ----
// Atrapa el foco dentro de un contenedor (panel de menú). Sustituye al foco atrapado del origen.
const TABBABLE = 'a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled])';

function trapFocus(container) {
    const items = Array.from(container.querySelectorAll(TABBABLE)).filter((el) => el.offsetParent !== null);
    if (!items.length) return;
    const first = items[0];
    const last = items[items.length - 1];
    setTimeout(() => first.focus(), 200);
    container.addEventListener('keydown', (event) => {
        if (event.key !== 'Tab') return;
        if (!event.shiftKey && document.activeElement === last) {
            event.preventDefault();
            first.focus();
        } else if (event.shiftKey && document.activeElement === first) {
            event.preventDefault();
            last.focus();
        }
    });
}

// ---- header ----
// Menú móvil y botón de contacto de la cabecera. Mismo contrato que el origen: `is-active`,
// `aria-expanded` y el foco atrapado dentro del panel abierto.


const PURPLE_BUTTON = ['bg-purple', 'text-white', 'hover:bg-purple-hover', 'focus:bg-purple-hover'];
const SKY_BUTTON = ['bg-sky-blue', 'text-deep-purple', 'hover:bg-sky-blue-hover', 'focus:bg-sky-blue-hover'];

function initHeader() {
    const menuButtons = document.querySelectorAll('.js-site-header-menu-button');
    const closeButton = document.querySelector('.js-site-header-close-menu-button');
    const overlay = document.querySelector('.js-overlay');
    const navWrapper = document.querySelector('.js-site-header-nav-wrapper');
    if (!navWrapper) return;

    const setExpanded = (value) => {
        menuButtons.forEach((b) => b.setAttribute('aria-expanded', value));
        closeButton?.setAttribute('aria-expanded', value);
    };
    const openMenu = () => {
        setExpanded('true');
        navWrapper.classList.add('is-active');
        overlay?.classList.add('is-active');
        trapFocus(navWrapper);
    };
    const closeMenu = () => {
        setExpanded('false');
        navWrapper.classList.remove('is-active');
        overlay?.classList.remove('is-active');
        menuButtons[0]?.focus();
    };

    menuButtons.forEach((b) => b.addEventListener('click', openMenu));
    closeButton?.addEventListener('click', closeMenu);
    overlay?.addEventListener('click', closeMenu);
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && navWrapper.classList.contains('is-active')) closeMenu();
    });
    document.addEventListener('click', (event) => {
        if (!navWrapper.classList.contains('is-active')) return;
        if (!event.target.closest('.js-site-header-nav-wrapper') && !event.target.closest('.js-site-header-menu-button')) closeMenu();
    });

    // El botón de contacto cambia de color salvo en héroes azules o morados oscuros (comportamiento del origen).
    const hero = document.querySelector('[data-hero]');
    const tone = hero?.getAttribute('data-hero');
    if (!['blue', 'dark-purple', 'purple'].includes(tone)) {
        document.querySelectorAll('.js-header-contact').forEach((el) => {
            el.classList.remove(...PURPLE_BUTTON);
            el.classList.add(...SKY_BUTTON);
        });
    }
}

// ---- page ----
// Comportamientos de página: ancla con desplazamiento suave, foco por teclado y parada de transiciones al redimensionar.

function initAnchors() {
    document.addEventListener('click', (event) => {
        const link = event.target.closest('a[href^="#"]:not(.has-dropdown)');
        if (!link) return;
        const target = document.querySelector(link.getAttribute('href'));
        if (!target) return;
        event.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
    if (window.location.hash) {
        window.addEventListener('load', () => {
            document.querySelector(window.location.hash)?.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
    }
}

// Tab marca la página como navegada por teclado; el ratón lo quita (salvo en controles que ya tienen foco visible).
function initKeyboardFocus() {
    const body = document.body;
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Tab') body.classList.add('is-keyboard-pressed');
    });
    document.addEventListener('mousedown', (event) => {
        if (event.target.matches('input[type=radio], input[type=checkbox], button, a[href="#"]')) return;
        body.classList.remove('is-keyboard-pressed');
    });
}

function initResizeStopper() {
    let timer;
    window.addEventListener('resize', () => {
        document.body.classList.add('u-resize-animation-stopper');
        clearTimeout(timer);
        timer = setTimeout(() => document.body.classList.remove('u-resize-animation-stopper'), 400);
    });
}

// ---- reveal ----
// Revelado al entrar en pantalla con IntersectionObserver (sustituye a la librería de animación del origen). Una sola vez por elemento.
function initReveal() {
    const items = document.querySelectorAll('[data-reveal]');
    if (!items.length) return;
    items.forEach((el) => {
        const delay = el.getAttribute('data-reveal-delay');
        if (delay) el.style.setProperty('--reveal-delay', `${delay}ms`);
    });
    if (!('IntersectionObserver' in window)) {
        items.forEach((el) => el.classList.add('is-revealed'));
        return;
    }
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (!entry.isIntersecting) return;
            entry.target.classList.add('is-revealed');
            observer.unobserve(entry.target);
        });
    }, { rootMargin: '0px 0px -120px 0px' });
    items.forEach((el) => observer.observe(el));
}

// ---- slider ----
// Carrusel de clientes con scroll-snap y botones propios. Sin JS, la pista es una fila desplazable.
// Anchos del origen (carrusel anterior): 1 ítem; 3 desde 700 px; 5 desde 980 px; separación de 20 px.
const GUTTER = 20;
const TRACK_SELECTOR = '.js-clients-slider';

function itemsPerView() {
    if (window.matchMedia('(min-width: 61.25em)').matches) return 5;
    if (window.matchMedia('(min-width: 43.75em)').matches) return 3;
    return 1;
}

function initClientsSlider() {
    const track = document.querySelector(TRACK_SELECTOR);
    if (!track) return;
    const slides = Array.from(track.querySelectorAll('.js-slider-item'));
    const prev = document.querySelector('.js-clients-slider-prev');
    const next = document.querySelector('.js-clients-slider-next');

    const layout = () => {
        const n = itemsPerView();
        const width = (track.clientWidth - GUTTER * (n - 1)) / n;
        slides.forEach((slide, i) => {
            slide.style.width = `${width}px`;
            slide.style.marginLeft = i === 0 ? '0px' : `${GUTTER}px`;
        });
    };
    const step = () => {
        const slide = slides[0];
        return slide ? slide.getBoundingClientRect().width + GUTTER : track.clientWidth;
    };
    prev?.addEventListener('click', () => track.scrollBy({ left: -step(), behavior: 'smooth' }));
    next?.addEventListener('click', () => track.scrollBy({ left: step(), behavior: 'smooth' }));
    layout();
    // Al fijar los anchos, el snap puede reubicar la pista: se vuelve al primer ítem.
    track.scrollLeft = 0;
    window.addEventListener('resize', layout);
}

// ---- modal ----
// Diálogo nativo para vídeo (YouTube) e imagen. Sustituye al plugin de modales: <dialog> con showModal(),
// cierre con el botón, con Escape y con clic fuera del contenido.

const VIDEO = '.video-modal-js';
const IMAGE = '.image-modal-js';

function initModal() {
    const dialog = document.querySelector('dialog.js-modal');
    if (!dialog) return;
    const content = dialog.querySelector('.js-modal-content');
    const close = dialog.querySelector('.js-modal-close');

    const open = (node) => {
        content.replaceChildren(node);
        dialog.showModal();
        close.focus();
    };
    document.addEventListener('click', (event) => {
        const video = event.target.closest(VIDEO);
        const image = event.target.closest(IMAGE);
        if (!video && !image) return;
        event.preventDefault();
        if (video) {
            const frame = document.createElement('iframe');
            frame.src = video.getAttribute('href');
            frame.title = 'Vídeo';
            frame.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture');
            frame.setAttribute('allowfullscreen', '');
            frame.className = 'aspect-video w-full';
            open(frame);
        } else {
            const img = document.createElement('img');
            img.src = image.getAttribute('href');
            img.alt = image.querySelector('img')?.getAttribute('alt') || '';
            img.className = 'block h-auto w-full';
            open(img);
        }
    });
    close.addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', (event) => {
        if (event.target === dialog) dialog.close();
    });
    dialog.addEventListener('close', () => content.replaceChildren());
}

// ---- forms ----
// Formularios de contacto. Sustituye a la validación y a los filtros de entrada del origen.
// Mensajes y reglas del origen (bundle de main.js): obligatorio, correo válido, y filtros por tipo de dato.

const MESSAGES = {
    required: 'Este campo es obligatorio.',
    email: 'Por favor, escribe una dirección de correo válida.',
};
const FILTERS = [
    ['.js-only-numbers', /^[0-9]*$/],
    ['.js-only-letters', /^[a-zA-ZáéíóúÁÉÍÓÚ'´ñÑäëïöüÄËÏÖÜ -]*$/],
    ['.js-only-alpha-numeric', /^[0-9a-zA-Z]*$/],
    ['.js-only-phone', /^[0-9-]*$/],
];
const FILTER_EVENTS = ['input', 'keydown', 'keyup', 'mousedown', 'mouseup', 'select', 'contextmenu', 'drop'];

function attachFilter(el, pattern) {
    FILTER_EVENTS.forEach((type) => {
        el.addEventListener(type, () => {
            if (pattern.test(el.value)) {
                el.dataset.oldValue = el.value;
            } else if ('oldValue' in el.dataset) {
                el.value = el.dataset.oldValue;
            }
        });
    });
}

function showError(field, text) {
    field.classList.add('js-form-error');
    const holder = field.type === 'checkbox'
        ? field.form.querySelector('.js-contact-form-checboxes-error') || field.parentElement
        : field.parentElement;
    let message = holder.querySelector('.js-form-error-message');
    if (!message) {
        message = document.createElement('p');
        message.className = 'js-form-error-message m-0 mt-2 text-14 text-red';
        holder.append(message);
    }
    message.textContent = text;
}

function clearError(field) {
    field.classList.remove('js-form-error');
    field.parentElement?.querySelector('.js-form-error-message')?.remove();
}

function validate(form) {
    let valid = true;
    form.querySelectorAll('input, textarea, select').forEach((field) => {
        if (field.disabled || !field.willValidate) return;
        clearError(field);
        if (field.checkValidity()) return;
        valid = false;
        const text = field.validity.typeMismatch ? MESSAGES.email : MESSAGES.required;
        showError(field, text);
    });
    return valid;
}

function initConditionals(form) {
    const business = form.querySelector('.js-contact-form-radio-business');
    const businessItem = form.querySelector('.js-business-item');
    const businessName = form.querySelector('.js-contact-form-business-name');
    const businessValue = business?.value;
    const syncBusiness = () => {
        if (!businessItem || !businessName) return;
        const isBusiness = business.checked;
        businessItem.classList.toggle('hidden', !isBusiness);
        businessName.disabled = !isBusiness;
    };
    form.querySelectorAll('.js-contact-form-radio-business, .js-contact-form-radio-person').forEach((radio) => {
        radio.addEventListener('change', () => {
            if (business) business.checked = radio.value === businessValue;
            syncBusiness();
        });
    });
    syncBusiness();

    const messageToggle = form.querySelector('.js-contact-form-checkbox-message');
    const textItem = form.querySelector('.js-textarea-item');
    const textarea = form.querySelector('.js-contact-form-textarea-message');
    const syncText = () => {
        if (!textItem || !textarea || !messageToggle) return;
        textItem.classList.toggle('hidden', !messageToggle.checked);
        textarea.disabled = !messageToggle.checked;
    };
    messageToggle?.addEventListener('change', syncText);
    syncText();
}

function initForms() {
    FILTERS.forEach(([selector, pattern]) => {
        document.querySelectorAll(selector).forEach((el) => attachFilter(el, pattern));
    });
    document.querySelectorAll('.js-form').forEach((form) => {
        initConditionals(form);
        form.addEventListener('submit', (event) => {
            if (!validate(form)) {
                event.preventDefault();
                return;
            }
            form.classList.add('js-form--loading');
            const submit = form.querySelector('[type=submit]');
            if (submit) submit.disabled = true;
        });
    });
}

// ---- arranque ----
initHeader();
initAnchors();
initKeyboardFocus();
initResizeStopper();
initReveal();
initClientsSlider();
initModal();
initForms();
