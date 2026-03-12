// Initialize Lucide icons
lucide.createIcons();

// Tabs Logic
function switchTab(tabId) {
    // Remove active classes
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.add('hidden');
        content.classList.remove('fade-in');
    });

    // Add active class to selected tab
    document.getElementById('tab-' + tabId).classList.add('active');
    
    // Show content with animation
    const content = document.getElementById('content-' + tabId);
    content.classList.remove('hidden');
    // small delay to restart animation
    setTimeout(() => {
        content.classList.add('fade-in');
    }, 10);
}
