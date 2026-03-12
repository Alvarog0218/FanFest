tailwind.config = {
    theme: {
        extend: {
            colors: {
                brand: {
                    black: '#000000',
                    dark: '#1D1D1B',
                    purple: '#7533FF',
                    lime: '#D5FC6B',
                    cream: '#FFFDEE',
                }
            },
            fontFamily: {
                sans: ['Inter', 'sans-serif'],
                heading: ['Outfit', 'sans-serif'],
            },
            boxShadow: {
                'glow': '0 0 20px rgba(213, 252, 107, 0.4)',
                'glow-lg': '0 0 30px rgba(213, 252, 107, 0.6)',
                'glow-purple': '0 0 20px rgba(117, 51, 255, 0.4)',
            }
        }
    }
}
