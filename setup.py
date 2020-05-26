from setuptools import setup, find_packages

setup(name='gym_call',
      packages = find_packages(),
      include_package_data = True,
      package_data = {
            '': ['*.csv', '*.npy']
      },
      version='0.0.1',
      install_requires=['gym', 'numpy', 'pandas', 'joblib']  # And any other dependencies foo needs
)