from setuptools import setup, Extension

def main():
    print("Compiling e_divisive.c...")
    setup(
        ext_modules=[
            Extension(
                "otava/signal_processing_algorithms/e_divisive/calculators._e_divisive",
                ["otava/signal_processing_algorithms/e_divisive/calculators/e_divisive.c"]
            )
        ],
        script_args=['build_ext', '--inplace']
    )

if __name__ == "__main__":
    main()
