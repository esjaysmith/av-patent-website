// Google Analytics 4 Configuration
// Replace 'GA_MEASUREMENT_ID' with your actual GA4 Measurement ID

(function() {
  // Load Google Analytics script
  var script = document.createElement('script');
  script.async = true;
  script.src = 'https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID';
  document.head.appendChild(script);

  // Initialize GA4
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');

  // Custom event tracking functions
  window.trackEvent = function(eventName, parameters) {
    gtag('event', eventName, parameters);
  };

  // Track form submissions
  window.trackFormSubmission = function(formName) {
    gtag('event', 'form_submission', {
      'form_name': formName
    });
  };

  // Track button clicks
  window.trackButtonClick = function(buttonName) {
    gtag('event', 'button_click', {
      'button_name': buttonName
    });
  };
})();