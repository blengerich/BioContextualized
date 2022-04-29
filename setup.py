import setuptools

setuptools.setup(name='BioContextualized',
      packages=[
        'BioContextualized',
        'BioContextualized.scContextualized',
        'BioContextualized.MedContextualized'
      ],
      version='0.0.0',
      install_requires=[
          'pytorch-lightning',
          'torch',
          'numpy',
          'tqdm',
          'scikit-learn',
          'python-igraph',
          'matplotlib',
          'pandas',
          'umap-learn',
          'interpret',
          'tensorflow>=2.4.0',
          'tensorflow-addons',
          'numpy>=1.19.2',
          'ipywidgets',
          'torchvision',
          'scanpy',
      ],
)
