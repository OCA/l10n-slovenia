import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo10-addons-oca-l10n-slovenia",
    description="Meta package for oca-l10n-slovenia Odoo addons",
    version=version,
    install_requires=[
        'odoo10-addon-l10n_si_upgraded',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 10.0',
    ]
)
