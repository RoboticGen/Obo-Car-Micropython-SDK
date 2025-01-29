# include default manifest
include("$(PORT_DIR)/boards/manifest.py")

# include our own extra...
module("obocar.py", base_path="$(BOARD_DIR)/../../src/obo-car") 
