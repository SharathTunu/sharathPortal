function copyEmail(email, tooltipId) {
  navigator.clipboard.writeText(email).then(() => {
    const tooltip = document.getElementById(tooltipId);
    if (tooltip) {
      tooltip.classList.add('show');
      setTimeout(() => {
        tooltip.classList.remove('show');
      }, 1500);
    }
  }).catch(err => {
    console.error('Failed to copy email:', err);
  });
}
