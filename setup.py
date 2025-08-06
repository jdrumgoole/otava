from setuptools import setup, Extension

print("Compiling e_divisive.c...")
setup(
    ext_modules=[
        Extension(
            "signal_processing_algorithms.energy_statistics.calculators._e_divisive",
            ["otava/signal_processing_algorithms/e_divisive/calculators/e_divisive.c"],
            optional=True,
        )
    ],
)