/**
 * Main JavaScript File
 * Autonomous Driving Patent Licensing Website
 * Modular architecture with component initialization
 */

// ===== MODULE SCOPE =====
(function() {
  'use strict';

  // ===== CONFIGURATION =====
  const CONFIG = {
    breakpoints: {
      sm: 640,
      md: 768,
      lg: 1024,
      xl: 1280
    },
    animations: {
      duration: 300,
      easing: 'ease-in-out'
    },
    forms: {
      validationDelay: 500
    }
  };

  // ===== UTILITY FUNCTIONS =====
  const Utils = {
    /**
     * Check if element is in viewport
     */
    isInViewport: function(element) {
      const rect = element.getBoundingClientRect();
      return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
      );
    },

    /**
     * Get current breakpoint
     */
    getCurrentBreakpoint: function() {
      const width = window.innerWidth;
      if (width >= CONFIG.breakpoints.xl) return 'xl';
      if (width >= CONFIG.breakpoints.lg) return 'lg';
      if (width >= CONFIG.breakpoints.md) return 'md';
      if (width >= CONFIG.breakpoints.sm) return 'sm';
      return 'xs';
    },

    /**
     * Debounce function calls
     */
    debounce: function(func, wait) {
      let timeout;
      return function executedFunction(...args) {
        const later = () => {
          clearTimeout(timeout);
          func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
      };
    },

    /**
     * Throttle function calls
     */
    throttle: function(func, limit) {
      let inThrottle;
      return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
          func.apply(context, args);
          inThrottle = true;
          setTimeout(() => inThrottle = false, limit);
        }
      };
    }
  };

  // ===== NAVIGATION MODULE =====
  const Navigation = {
    init: function() {
      this.bindEvents();
      this.setupMobileMenu();
    },

    bindEvents: function() {
      // Smooth scrolling for anchor links
      document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
          e.preventDefault();
          const target = document.querySelector(anchor.getAttribute('href'));
          if (target) {
            target.scrollIntoView({
              behavior: 'smooth',
              block: 'start'
            });
          }
        });
      });
    },

    setupMobileMenu: function() {
      const toggle = document.querySelector('.mobile-menu-toggle');
      const menu = document.querySelector('.nav-menu');

      if (toggle && menu) {
        toggle.addEventListener('click', () => {
          menu.classList.toggle('active');
          toggle.classList.toggle('active');
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
          if (!menu.contains(e.target) && !toggle.contains(e.target)) {
            menu.classList.remove('active');
            toggle.classList.remove('active');
          }
        });

        // Close menu on window resize
        window.addEventListener('resize', Utils.debounce(() => {
          if (Utils.getCurrentBreakpoint() !== 'xs') {
            menu.classList.remove('active');
            toggle.classList.remove('active');
          }
        }, 250));
      }
    }
  };

  // ===== FORM VALIDATION MODULE =====
  const FormValidation = {
    init: function() {
      this.bindEvents();
    },

    bindEvents: function() {
      // Real-time validation
      document.querySelectorAll('.form-control').forEach(input => {
        input.addEventListener('blur', (e) => {
          this.validateField(e.target);
        });

        input.addEventListener('input', Utils.debounce((e) => {
          this.validateField(e.target);
        }, CONFIG.forms.validationDelay));
      });

      // Form submission
      document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', (e) => {
          this.handleSubmit(e);
        });
      });
    },

    validateField: function(field) {
      const value = field.value.trim();
      const isRequired = field.hasAttribute('required');
      let isValid = true;
      let message = '';

      // Clear previous validation
      this.clearFieldValidation(field);

      // Required field validation
      if (isRequired && !value) {
        isValid = false;
        message = 'This field is required';
      }

      // Email validation
      if (field.type === 'email' && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
          isValid = false;
          message = 'Please enter a valid email address';
        }
      }

      // Phone validation (optional)
      if (field.type === 'tel' && value) {
        const phoneRegex = /^[\+]?[1-9][\d]{0,15}$/;
        if (!phoneRegex.test(value.replace(/[\s\-\(\)]/g, ''))) {
          isValid = false;
          message = 'Please enter a valid phone number';
        }
      }

      // Update field appearance
      if (!isValid) {
        field.classList.add('is-invalid');
        this.showFieldError(field, message);
      } else if (value) {
        field.classList.add('is-valid');
      }

      return isValid;
    },

    clearFieldValidation: function(field) {
      field.classList.remove('is-invalid', 'is-valid');
      const errorElement = field.parentNode.querySelector('.error-message');
      if (errorElement) {
        errorElement.remove();
      }
    },

    showFieldError: function(field, message) {
      const errorElement = document.createElement('div');
      errorElement.className = 'error-message';
      errorElement.textContent = message;
      field.parentNode.appendChild(errorElement);
    },

    handleSubmit: function(e) {
      e.preventDefault();
      const form = e.target;
      const submitButton = form.querySelector('button[type="submit"]');
      const originalText = submitButton.textContent;

      // Validate all fields
      let isFormValid = true;
      form.querySelectorAll('.form-control').forEach(field => {
        if (!this.validateField(field)) {
          isFormValid = false;
        }
      });

      if (!isFormValid) {
        // Scroll to first error
        const firstError = form.querySelector('.is-invalid');
        if (firstError) {
          firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
          firstError.focus();
        }
        return;
      }

      // Show loading state
      submitButton.disabled = true;
      submitButton.innerHTML = '<span class="loading-spinner"></span> Sending...';

      // Simulate form submission (replace with actual API call)
      setTimeout(() => {
        this.showFormMessage(form, 'success', 'Thank you! Your message has been sent successfully.');
        submitButton.disabled = false;
        submitButton.textContent = originalText;
        form.reset();

        // Clear validation states
        form.querySelectorAll('.form-control').forEach(field => {
          this.clearFieldValidation(field);
        });
      }, 2000);
    },

    showFormMessage: function(form, type, message) {
      // Remove existing messages
      const existingMessage = form.querySelector('.form-message');
      if (existingMessage) {
        existingMessage.remove();
      }

      // Create new message
      const messageElement = document.createElement('div');
      messageElement.className = `form-message ${type}`;
      messageElement.innerHTML = `<p>${message}</p>`;

      // Insert after form
      form.parentNode.insertBefore(messageElement, form.nextSibling);

      // Auto-remove after 5 seconds
      setTimeout(() => {
        if (messageElement.parentNode) {
          messageElement.remove();
        }
      }, 5000);
    }
  };

  // ===== ACCORDION MODULE =====
  const Accordion = {
    init: function() {
      this.bindEvents();
    },

    bindEvents: function() {
      document.querySelectorAll('.accordion-button').forEach(button => {
        button.addEventListener('click', (e) => {
          this.toggleAccordion(e.target);
        });
      });
    },

    toggleAccordion: function(button) {
      const item = button.closest('.accordion-item');
      const content = item.querySelector('.accordion-content');
      const isActive = content.classList.contains('active');

      // Close all accordions in the same group
      const accordion = item.closest('.accordion');
      accordion.querySelectorAll('.accordion-content').forEach(content => {
        content.classList.remove('active');
      });
      accordion.querySelectorAll('.accordion-button').forEach(btn => {
        btn.classList.remove('active');
      });

      // Open clicked accordion if it wasn't active
      if (!isActive) {
        content.classList.add('active');
        button.classList.add('active');
      }
    }
  };

  // ===== MODAL MODULE =====
  const Modal = {
    init: function() {
      this.bindEvents();
    },

    bindEvents: function() {
      // Modal triggers
      document.querySelectorAll('[data-modal]').forEach(trigger => {
        trigger.addEventListener('click', (e) => {
          e.preventDefault();
          const modalId = trigger.getAttribute('data-modal');
          this.openModal(modalId);
        });
      });

      // Modal close buttons
      document.querySelectorAll('.modal-close, .modal-overlay').forEach(close => {
        close.addEventListener('click', (e) => {
          if (e.target === close || e.target.classList.contains('modal-overlay')) {
            this.closeModal();
          }
        });
      });

      // ESC key to close modal
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
          this.closeModal();
        }
      });
    },

    openModal: function(modalId) {
      const modal = document.getElementById(modalId);
      if (modal) {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';

        // Focus management
        const focusableElements = modal.querySelectorAll(
          'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
        );
        if (focusableElements.length) {
          focusableElements[0].focus();
        }
      }
    },

    closeModal: function() {
      const activeModal = document.querySelector('.modal-overlay.active');
      if (activeModal) {
        activeModal.classList.remove('active');
        document.body.style.overflow = '';
      }
    }
  };

  // ===== ANIMATION MODULE =====
  const Animation = {
    init: function() {
      this.bindEvents();
      this.initScrollAnimations();
    },

    bindEvents: function() {
      // Add loading class to body initially
      document.body.classList.add('loading');

      // Remove loading class when page is loaded
      window.addEventListener('load', () => {
        document.body.classList.remove('loading');
        this.animateOnLoad();
      });
    },

    initScrollAnimations: function() {
      const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
      };

      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('animate-in');
          }
        });
      }, observerOptions);

      // Observe elements with animation classes
      document.querySelectorAll('[class*="animate-"]').forEach(element => {
        observer.observe(element);
      });
    },

    animateOnLoad: function() {
      // Stagger animations for hero elements
      const heroElements = document.querySelectorAll('.hero h1, .hero .hero-subtitle, .hero .hero-stats, .hero .hero-ctas');
      heroElements.forEach((element, index) => {
        setTimeout(() => {
          element.style.opacity = '1';
          element.style.transform = 'translateY(0)';
        }, index * 200);
      });
    }
  };

  // ===== ANALYTICS MODULE =====
  const Analytics = {
    init: function() {
      this.bindEvents();
    },

    bindEvents: function() {
      // Track button clicks
      document.querySelectorAll('.btn').forEach(button => {
        button.addEventListener('click', (e) => {
          this.trackEvent('button_click', {
            button_text: e.target.textContent.trim(),
            button_location: this.getElementLocation(e.target)
          });
        });
      });

      // Track form submissions
      document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', (e) => {
          this.trackEvent('form_submit', {
            form_name: form.getAttribute('name') || form.id || 'unknown'
          });
        });
      });

      // Track outbound links
      document.querySelectorAll('a[href^="http"]').forEach(link => {
        link.addEventListener('click', (e) => {
          this.trackEvent('outbound_link', {
            link_url: e.target.href,
            link_text: e.target.textContent.trim()
          });
        });
      });
    },

    trackEvent: function(eventName, parameters) {
      // Google Analytics 4 tracking
      if (typeof gtag !== 'undefined') {
        gtag('event', eventName, parameters);
      }

      // Console logging for development
      if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
        console.log('Analytics Event:', eventName, parameters);
      }
    },

    getElementLocation: function(element) {
      // Get element's position in DOM for context
      const sections = ['hero', 'header', 'footer', 'sidebar'];
      for (const section of sections) {
        if (element.closest(`.${section}`)) {
          return section;
        }
      }
      return 'content';
    }
  };

  // ===== ACCESSIBILITY MODULE =====
  const Accessibility = {
    init: function() {
      this.setupSkipLinks();
      this.setupFocusManagement();
      this.setupKeyboardNavigation();
    },

    setupSkipLinks: function() {
      // Add skip to main content link
      const skipLink = document.createElement('a');
      skipLink.href = '#main-content';
      skipLink.className = 'sr-only skip-link';
      skipLink.textContent = 'Skip to main content';
      document.body.insertBefore(skipLink, document.body.firstChild);

      // Show skip link on focus
      skipLink.addEventListener('focus', () => {
        skipLink.style.top = '0';
      });

      skipLink.addEventListener('blur', () => {
        skipLink.style.top = '-40px';
      });
    },

    setupFocusManagement: function() {
      // Ensure main content has proper ID
      const main = document.querySelector('main') || document.querySelector('#main-content');
      if (main && !main.id) {
        main.id = 'main-content';
      }
    },

    setupKeyboardNavigation: function() {
      // Enhanced keyboard navigation for interactive elements
      document.addEventListener('keydown', (e) => {
        // Close modals with ESC
        if (e.key === 'Escape') {
          const activeModal = document.querySelector('.modal-overlay.active');
          if (activeModal) {
            Modal.closeModal();
          }
        }
      });
    }
  };

  // ===== PERFORMANCE MODULE =====
  const Performance = {
    init: function() {
      this.lazyLoadImages();
      this.optimizeScroll();
    },

    lazyLoadImages: function() {
      const images = document.querySelectorAll('img[data-src]');

      if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              const img = entry.target;
              img.src = img.dataset.src;
              img.classList.remove('lazy');
              imageObserver.unobserve(img);
            }
          });
        });

        images.forEach(img => imageObserver.observe(img));
      } else {
        // Fallback for browsers without IntersectionObserver
        images.forEach(img => {
          img.src = img.dataset.src;
        });
      }
    },

    optimizeScroll: function() {
      // Throttle scroll events
      let scrollTimeout;
      window.addEventListener('scroll', Utils.throttle(() => {
        this.handleScroll();
      }, 16)); // ~60fps
    },

    handleScroll: function() {
      // Add scrolled class to body for styling
      if (window.scrollY > 50) {
        document.body.classList.add('scrolled');
      } else {
        document.body.classList.remove('scrolled');
      }

      // Update active navigation based on scroll position
      this.updateActiveNavigation();
    },

    updateActiveNavigation: function() {
      const sections = document.querySelectorAll('section[id]');
      const navLinks = document.querySelectorAll('.nav-link[href^="#"]');

      let current = '';
      sections.forEach(section => {
        const sectionTop = section.offsetTop;
        if (window.scrollY >= sectionTop - 60) {
          current = section.getAttribute('id');
        }
      });

      navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
          link.classList.add('active');
        }
      });
    }
  };

  // ===== INITIALIZATION =====
  document.addEventListener('DOMContentLoaded', function() {
    // Initialize all modules
    Navigation.init();
    FormValidation.init();
    Accordion.init();
    Modal.init();
    Animation.init();
    Analytics.init();
    Accessibility.init();
    Performance.init();

    // Log initialization for debugging
    if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
      console.log('Website JavaScript initialized successfully');
    }
  });

  // ===== GLOBAL API =====
  window.Website = {
    Utils: Utils,
    Navigation: Navigation,
    FormValidation: FormValidation,
    Accordion: Accordion,
    Modal: Modal,
    Animation: Animation,
    Analytics: Analytics,
    Accessibility: Accessibility,
    Performance: Performance
  };

})();