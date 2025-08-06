"""
Prompt Factory Generator - Custom ComfyUI nodes for advanced prompt generation
"""

# Display startup message in yellow
print("\033[93m🏭 The assembly line is live.\033[0m")

from .Factory_prompt_generator import NODE_CLASS_MAPPINGS as PROMPT_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as PROMPT_DISPLAY_MAPPINGS
from .Factory_negative_generator import NODE_CLASS_MAPPINGS as NEGATIVE_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as NEGATIVE_DISPLAY_MAPPINGS

# Combine all node mappings
NODE_CLASS_MAPPINGS = {**PROMPT_MAPPINGS, **NEGATIVE_MAPPINGS}
NODE_DISPLAY_NAME_MAPPINGS = {**PROMPT_DISPLAY_MAPPINGS, **NEGATIVE_DISPLAY_MAPPINGS}

# Export node mappings
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
