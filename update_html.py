import codecs

with codecs.open('d:\\Dev\\FanFest\\index.html', 'r', 'utf-8') as f:
    html = f.read()

# Make the changes requested
replacements = {
    'btn-gold': 'btn-primary',
    'bg-slate-950': 'bg-brand-black',
    'bg-slate-900': 'bg-brand-dark',
    'border-slate-800/50': 'border-brand-dark',
    'bg-slate-800': 'bg-[#2a2a26]',
    'border-slate-700': 'border-[#2a2a26]',
    'border-slate-600': 'border-brand-purple/30',
    'text-slate-200': 'text-brand-cream',
    'text-slate-300': 'text-brand-cream/80',
    'text-slate-400': 'text-brand-cream/60',
    'text-slate-500': 'text-brand-cream/40',
    'text-slate-600': 'text-brand-cream/30',
    'text-white': 'text-brand-cream',
    
    # Old Accent colors
    'amber-400': 'brand-lime',
    'amber-500': 'brand-purple',
    'amber-600': 'brand-purple',
    
    # Yellow (Gold Sponsor)
    'text-yellow-400': 'text-brand-lime',
    'border-yellow-400': 'border-brand-purple',
    'yellow-400': 'brand-purple',
    
    # Green (Expositor)
    'text-green-400': 'text-brand-purple',
    'border-green-500': 'border-brand-purple',
    'green-400': 'brand-purple',
    
    # Blue shadow
    'bg-blue-500': 'bg-brand-purple',
    
    # RGB Shadows & borders
    'rgba(251,191,36': 'rgba(213,252,107',
    'rgba(251, 191, 36': 'rgba(213, 252, 107',
    'rgba(250,204,21': 'rgba(117,51,255',
}

for old, new in replacements.items():
    html = html.replace(old, new)

# specific fixes
html = html.replace('shadow-[0_0_20px_rgba(213,252,107,0.2)]', 'shadow-[0_0_20px_rgba(117,51,255,0.2)]')
html = html.replace('border-brand-lime/20', 'border-brand-purple/20')
html = html.replace('bg-brand-purple/5', 'bg-brand-purple/10')
html = html.replace('hover:border-brand-purple/30', 'hover:border-brand-lime/30')

with codecs.open('d:\\Dev\\FanFest\\index.html', 'w', 'utf-8') as f:
    f.write(html)
