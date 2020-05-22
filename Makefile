
## ========================================================================= ##

# -------------------------------- Variables -------------------------------- #

# C compiler.
CC             	:= gcc

# Language standard.
C_STANDARD    	:= gnu17

# C Compiler flags. #-DMACRO=_GNU_SOURCE 
CFLAGS       		:= -O2 -pedantic -Wall -std=$(C_STANDARD)

# Header files directory ".h", ".H", ".hh", ".hpp".
INCLUDE_PATH    := -Iinclude

# Linking flags.
LDFLAGS					:= -static

# Binary target directory.
BINDIR				  := bin

# Binary target name.
TARGET          := $(BINDIR)/aswap

# Source files extension.
SRCEXT          := c

# Source files directory fonte ".cpp", ".cxx", ".cc".
SRCDIR          := src

# Object files directory.
OBJDIR					:= build

# Object files list.
OBJECTS 				:= $(OBJDIR)/aswap.o

# ---------------------------------- Rules ---------------------------------- #

# Binary linking.
$(TARGET): $(OBJECTS)
	$(CC) $^ -o $(TARGET) $(LDFLAGS)

# Object compilation.
$(OBJDIR)/%.o: $(SRCDIR)/%.$(SRCEXT) include/%.h
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) $(INCLUDE_PATH) -c -o $@ $<

# Clean objects and binary.
clean:
	$(RM) -r $(OBJDIR)/*.o $(TARGET)

# Avoid headaches
.PHONY: clean

## ========================================================================= ##