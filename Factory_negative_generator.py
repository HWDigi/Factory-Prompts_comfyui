import random
from typing import List, Dict, Any


class FactoryPromptsNegativeGenerator:
    """
    Comprehensive negative prompt generator for all checkpoint types
    Provides categorized negative prompts for quality control and style management
    """
    
    def __init__(self):
        # Base quality negatives - always included
        self.base_quality = [
            "lowres", "bad_anatomy", "bad_hands", "text", "error",
            "missing_fingers", "extra_digit", "fewer_digits", "cropped",
            "worst_quality", "low_quality", "normal_quality", 
            "jpeg_artifacts", "signature", "watermark", "username", "blurry"
        ]
        
        # Enhanced quality negatives for higher standards
        self.enhanced_quality = [
            "bad_proportions", "bad_perspective", "bad_shading",
            "bad_composition", "bad_lighting", "overexposed", "underexposed",
            "noise", "grainy", "pixelated", "compression_artifacts",
            "aliasing", "distorted", "deformed", "malformed"
        ]
        
        # Anatomy and body negatives
        self.anatomy_negatives = [
            "bad_anatomy", "bad_hands", "bad_feet", "bad_face",
            "missing_fingers", "extra_digit", "fewer_digits", "extra_fingers",
            "mutated_hands", "poorly_drawn_hands", "poorly_drawn_face",
            "mutation", "deformed", "ugly", "blurry_face", "disfigured",
            "extra_limbs", "missing_limbs", "extra_arms", "missing_arms",
            "extra_legs", "missing_legs", "fused_fingers", "too_many_fingers",
            "long_neck", "duplicate", "morbid", "mutilated", "extra_head",
            "poorly_drawn_eyes", "bad_eyes", "crossed_eyes", "extra_tongue",
            "multiple_tongues", "deformed_tongue", "elongated_tongue"
        ]
        
        # Non-realistic style control negatives
        self.non_realistic_style_control = [
            "source_cartoon", "source_furry", "source_pony", "western_comic",
            "cartoon", "disney", "pixar", "anime_style", "manga_style",
            "chibi", "cel_shading", "flat_colors", "simplified_art"
        ]
        
        # Realistic style control negatives  
        self.realistic_style_control = [
            "3d", "realistic", "photorealistic", "photo", "photography",
            "real_person", "live_action", "cgi", "render", "blender", 
            "unreal_engine", "ray_tracing", "hyperrealistic", "lifelike"
        ]
        
        # Art medium negatives
        self.unwanted_mediums = [
            "sketch", "pencil_sketch", "rough_sketch", "draft",
            "unfinished", "incomplete", "work_in_progress", "wip",
            "traditional_media", "pencil_drawing", "charcoal",
            "crayon", "chalk", "pastel", "watercolor_paper",
            "canvas_texture", "paper_texture", "scan_artifacts"
        ]
        
        # Color and saturation control
        self.color_negatives = [
            "monochrome", "grayscale", "greyscale", "black_and_white",
            "sepia", "desaturated", "oversaturated", "color_bleeding",
            "bad_colors", "ugly_colors", "neon_colors", "garish",
            "overexposed_colors", "washed_out", "faded_colors"
        ]
        
        # Composition and framing negatives
        self.composition_negatives = [
            "bad_composition", "bad_framing", "cut_off", "cropped_head",
            "cropped_body", "out_of_frame", "off_center", "unbalanced",
            "awkward_pose", "stiff_pose", "unnatural_pose", "forced_smile",
            "bad_perspective", "wrong_perspective", "floating"
        ]
        
        # Background and environment negatives
        self.background_negatives = [
            "cluttered_background", "busy_background", "distracting_background",
            "bad_background", "messy_background", "noisy_background",
            "artifacts_in_background", "floating_objects", "inconsistent_lighting",
            "multiple_light_sources", "confusing_background"
        ]
        
        # Text and UI element negatives
        self.text_negatives = [
            "text", "words", "letters", "numbers", "symbols",
            "watermark", "signature", "artist_name", "copyright",
            "logo", "brand", "website", "url", "username",
            "speech_bubble", "thought_bubble", "text_bubble",
            "caption", "subtitle", "overlay_text", "ui_elements"
        ]
        
        # Clothing and fashion negatives
        self.clothing_negatives = [
            "bad_clothing", "poorly_drawn_clothes", "floating_clothes",
            "clipping_clothes", "transparent_clothes", "see_through_clothes",
            "torn_clothes", "damaged_clothes", "wrinkled_clothes",
            "ill_fitting_clothes", "oversized_clothes", "undersized_clothes"
        ]
        
        # Expression and emotion negatives
        self.expression_negatives = [
            "dead_eyes", "empty_eyes", "soulless_eyes", "scary_eyes",
            "angry_expression", "sad_expression", "depressed_expression",
            "forced_expression", "unnatural_expression", "blank_expression",
            "emotionless", "creepy_smile", "evil_smile"
        ]
        
        # Hair negatives
        self.hair_negatives = [
            "bad_hair", "poorly_drawn_hair", "floating_hair", "messy_hair",
            "tangled_hair", "unrealistic_hair", "bad_hair_physics",
            "clipping_hair", "hair_artifacts", "inconsistent_hair_color"
        ]
        
        # NSFW content filters (for SFW generations)
        self.nsfw_filters = [
            "nsfw", "explicit", "nude", "naked", "topless", "bottomless",
            "underwear", "lingerie", "bikini", "swimsuit", "revealing_clothes",
            "cleavage", "exposed_skin", "suggestive", "provocative",
            "sexual", "erotic", "adult_content", "mature_content"
        ]
        
        # Violence and disturbing content filters
        self.violence_filters = [
            "violence", "blood", "gore", "death", "killing", "murder",
            "torture", "pain", "suffering", "injury", "wound", "scar",
            "bruise", "cut", "bleeding", "dark_themes", "disturbing",
            "nightmare", "horror", "scary", "frightening"
        ]
        
        # Technical artifact negatives
        self.technical_negatives = [
            "compression_artifacts", "jpeg_artifacts", "aliasing", "moire",
            "banding", "posterization", "color_banding", "pixelation",
            "blur_artifacts", "sharpening_artifacts", "noise_artifacts",
            "upscaling_artifacts", "interpolation_artifacts"
        ]

    def get_base_negatives(self) -> List[str]:
        """Always included base negative prompts"""
        return self.base_quality.copy()

    def get_category_negatives(self, categories: List[str]) -> List[str]:
        """Get negatives from specific categories"""
        negatives = []
        
        category_map = {
            "enhanced_quality": self.enhanced_quality,
            "anatomy": self.anatomy_negatives,
            "non_realistic_style_control": self.non_realistic_style_control,
            "realistic_style_control": self.realistic_style_control,
            "unwanted_mediums": self.unwanted_mediums,
            "color_control": self.color_negatives,
            "composition": self.composition_negatives,
            "background": self.background_negatives,
            "text_elements": self.text_negatives,
            "clothing": self.clothing_negatives,
            "expressions": self.expression_negatives,
            "hair": self.hair_negatives,
            "nsfw_filters": self.nsfw_filters,
            "violence_filters": self.violence_filters,
            "technical": self.technical_negatives
        }
        
        for category in categories:
            if category in category_map:
                negatives.extend(category_map[category])
        
        return negatives

    def build_negative_prompt(self, 
                            preset: str = "standard",
                            custom_categories: List[str] = None,
                            include_style_control: bool = True,
                            include_nsfw_filters: bool = False,
                            include_violence_filters: bool = False,
                            custom_negatives: str = "",
                            strength_boost: bool = False) -> str:
        """
        Build comprehensive negative prompt based on settings
        
        Args:
            preset: Predefined negative prompt preset
            custom_categories: List of specific categories to include
            include_style_control: Add style control negatives
            include_nsfw_filters: Add NSFW content filters
            include_violence_filters: Add violence/disturbing content filters
            custom_negatives: Additional custom negative terms
            strength_boost: Add emphasis to critical negatives
        """
        
        negatives = self.get_base_negatives()
        
        # Apply presets
        if preset == "minimal":
            # Just base quality negatives
            pass
        elif preset == "standard":
            negatives.extend(self.get_category_negatives([
                "enhanced_quality", "anatomy", "composition", "text_elements"
            ]))
        elif preset == "comprehensive":
            negatives.extend(self.get_category_negatives([
                "enhanced_quality", "anatomy", "composition", "background",
                "text_elements", "clothing", "hair", "technical"
            ]))
        elif preset == "professional":
            negatives.extend(self.get_category_negatives([
                "enhanced_quality", "anatomy", "composition", "background",
                "text_elements", "clothing", "expressions", "hair", 
                "unwanted_mediums", "technical"
            ]))
        elif preset == "anime_focused":
            negatives.extend(self.get_category_negatives([
                "enhanced_quality", "anatomy", "non_realistic_style_control", "composition",
                "text_elements", "unwanted_mediums"
            ]))
        
        # Add custom categories
        if custom_categories:
            negatives.extend(self.get_category_negatives(custom_categories))
        
        # Add optional filters
        if include_style_control:
            negatives.extend(self.non_realistic_style_control)
            negatives.extend(self.realistic_style_control)
        
        if include_nsfw_filters:
            negatives.extend(self.nsfw_filters)
        
        if include_violence_filters:
            negatives.extend(self.violence_filters)
        
        # Add custom negatives
        if custom_negatives.strip():
            custom_terms = [term.strip() for term in custom_negatives.split(",") if term.strip()]
            negatives.extend(custom_terms)
        
        # Remove duplicates while preserving order
        seen = set()
        unique_negatives = []
        for negative in negatives:
            if negative not in seen:
                unique_negatives.append(negative)
                seen.add(negative)
        
        # Apply strength boost to critical terms
        if strength_boost:
            critical_terms = ["bad_anatomy", "bad_hands", "bad_face", "worst_quality", "low_quality"]
            boosted_negatives = []
            for negative in unique_negatives:
                if negative in critical_terms:
                    boosted_negatives.append(f"({negative}:1.2)")
                else:
                    boosted_negatives.append(negative)
            unique_negatives = boosted_negatives
        
        return ", ".join(unique_negatives)

    def get_preset_description(self, preset: str) -> str:
        """Get description of what each preset includes"""
        descriptions = {
            "minimal": "Basic quality control only - fastest generation",
            "standard": "Quality + anatomy + composition + text removal",
            "comprehensive": "Standard + background + clothing + hair + technical",
            "professional": "Comprehensive + expressions + unwanted mediums",
            "anime_focused": "Optimized for anime style with strong style control"
        }
        return descriptions.get(preset, "Unknown preset")


class PonyNegativeNode:
    """ComfyUI Node for Pony Negative Prompt Generation"""
    
    CATEGORY = "Prompt Factory"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("negative_prompt",)
    FUNCTION = "generate_negative"
    
    def __init__(self):
        self.generator = FactoryPromptsNegativeGenerator()
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset": (["minimal", "standard", "comprehensive", "professional", "anime_focused"], {"default": "standard"}),
                "include_style_control": ("BOOLEAN", {"default": True}),
                "include_nsfw_filters": ("BOOLEAN", {"default": False}),
                "include_violence_filters": ("BOOLEAN", {"default": False}),
                "strength_boost": ("BOOLEAN", {"default": False}),
            },
            "optional": {
                "custom_negatives": ("STRING", {"multiline": True, "default": ""}),
                "extra_categories": (["none", "enhanced_quality", "anatomy", "unwanted_mediums", 
                                   "color_control", "composition", "background", "text_elements", 
                                   "clothing", "expressions", "hair", "technical"], {"default": "none"}),
            }
        }
    
    def generate_negative(self, preset, include_style_control, include_nsfw_filters, 
                         include_violence_filters, strength_boost, custom_negatives="", 
                         extra_categories="none"):
        
        # Convert extra_categories to list
        extra_cats = [extra_categories] if extra_categories != "none" else []
        
        # Generate negative prompt
        negative = self.generator.build_negative_prompt(
            preset=preset,
            custom_categories=extra_cats,
            include_style_control=include_style_control,
            include_nsfw_filters=include_nsfw_filters,
            include_violence_filters=include_violence_filters,
            custom_negatives=custom_negatives,
            strength_boost=strength_boost
        )
        
        return (negative,)


class PonyNegativeCategorizedNode:
    """Advanced ComfyUI Node for Categorized Negative Prompt Control"""
    
    CATEGORY = "Prompt Factory"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("negative_prompt",)
    FUNCTION = "generate_categorized_negative"
    
    def __init__(self):
        self.generator = FactoryPromptsNegativeGenerator()
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_quality": ("BOOLEAN", {"default": True}),
                "enhanced_quality": ("BOOLEAN", {"default": True}),
                "anatomy_control": ("BOOLEAN", {"default": True}),
                "non_realistic_style_control": ("BOOLEAN", {"default": True}),
                "realistic_style_control": ("BOOLEAN", {"default": False}),
                "composition": ("BOOLEAN", {"default": True}),
                "text_removal": ("BOOLEAN", {"default": True}),
            },
            "optional": {
                "unwanted_mediums": ("BOOLEAN", {"default": False}),
                "color_control": ("BOOLEAN", {"default": False}),
                "background_control": ("BOOLEAN", {"default": False}),
                "clothing_control": ("BOOLEAN", {"default": False}),
                "expression_control": ("BOOLEAN", {"default": False}),
                "hair_control": ("BOOLEAN", {"default": False}),
                "nsfw_filters": ("BOOLEAN", {"default": False}),
                "violence_filters": ("BOOLEAN", {"default": False}),
                "technical_artifacts": ("BOOLEAN", {"default": False}),
                "strength_boost": ("BOOLEAN", {"default": False}),
                "custom_negatives": ("STRING", {"multiline": True, "default": ""}),
            }
        }
    
    def generate_categorized_negative(self, base_quality, enhanced_quality, anatomy_control,
                                    non_realistic_style_control, realistic_style_control, composition, text_removal, unwanted_mediums=False,
                                    color_control=False, background_control=False, clothing_control=False,
                                    expression_control=False, hair_control=False, nsfw_filters=False,
                                    violence_filters=False, technical_artifacts=False, strength_boost=False,
                                    custom_negatives=""):
        
        negatives = []
        
        # Add base categories based on selections
        if base_quality:
            negatives.extend(self.generator.get_base_negatives())
        
        # Build category list
        categories = []
        if enhanced_quality:
            categories.append("enhanced_quality")
        if anatomy_control:
            categories.append("anatomy")
        if unwanted_mediums:
            categories.append("unwanted_mediums")
        if color_control:
            categories.append("color_control")
        if composition:
            categories.append("composition")
        if background_control:
            categories.append("background")
        if text_removal:
            categories.append("text_elements")
        if clothing_control:
            categories.append("clothing")
        if expression_control:
            categories.append("expressions")
        if hair_control:
            categories.append("hair")
        if technical_artifacts:
            categories.append("technical")
        
        # Add category negatives
        negatives.extend(self.generator.get_category_negatives(categories))
        
        # Add optional style control filters
        if non_realistic_style_control:
            negatives.extend(self.generator.non_realistic_style_control)
        if realistic_style_control:
            negatives.extend(self.generator.realistic_style_control)
        if nsfw_filters:
            negatives.extend(self.generator.nsfw_filters)
        if violence_filters:
            negatives.extend(self.generator.violence_filters)
        
        # Add custom negatives
        if custom_negatives.strip():
            custom_terms = [term.strip() for term in custom_negatives.split(",") if term.strip()]
            negatives.extend(custom_terms)
        
        # Remove duplicates
        seen = set()
        unique_negatives = []
        for negative in negatives:
            if negative not in seen:
                unique_negatives.append(negative)
                seen.add(negative)
        
        # Apply strength boost
        if strength_boost:
            critical_terms = ["bad_anatomy", "bad_hands", "bad_face", "worst_quality", "low_quality"]
            boosted_negatives = []
            for negative in unique_negatives:
                if negative in critical_terms:
                    boosted_negatives.append(f"({negative}:1.2)")
                else:
                    boosted_negatives.append(negative)
            unique_negatives = boosted_negatives
        
        return (", ".join(unique_negatives),)


class PonyNegativeToggleNode:
    """Comprehensive ComfyUI Node for Negative Prompt Control with Individual Toggles"""
    
    CATEGORY = "Prompt Factory"
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("negative_prompt", "selected_categories")
    FUNCTION = "generate_negative_toggles"
    
    def __init__(self):
        self.generator = FactoryPromptsNegativeGenerator()
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
            "optional": {
                # Quality Control Toggles
                "base_quality": ("BOOLEAN", {"default": True}),
                "enhanced_quality": ("BOOLEAN", {"default": False}),
                "technical_artifacts": ("BOOLEAN", {"default": False}),
                
                # Anatomy Control Toggles
                "anatomy_control": ("BOOLEAN", {"default": True}),
                "expression_control": ("BOOLEAN", {"default": False}),
                "hair_control": ("BOOLEAN", {"default": False}),
                
                # Style Control Toggles
                "non_realistic_style_control": ("BOOLEAN", {"default": True}),
                "realistic_style_control": ("BOOLEAN", {"default": False}),
                "unwanted_mediums": ("BOOLEAN", {"default": False}),
                "color_control": ("BOOLEAN", {"default": False}),
                
                # Composition Toggles
                "composition": ("BOOLEAN", {"default": True}),
                "background_control": ("BOOLEAN", {"default": False}),
                "text_removal": ("BOOLEAN", {"default": True}),
                
                # Content Toggles
                "clothing_control": ("BOOLEAN", {"default": False}),
                "nsfw_filters": ("BOOLEAN", {"default": False}),
                "violence_filters": ("BOOLEAN", {"default": False}),
                
                # Enhancement Options
                "strength_boost": ("BOOLEAN", {"default": False}),
                "custom_negatives": ("STRING", {"multiline": True, "default": ""}),
            }
        }
    
    def generate_negative_toggles(self, seed, base_quality=True, enhanced_quality=False, 
                                 technical_artifacts=False, anatomy_control=True, 
                                 expression_control=False, hair_control=False, 
                                 non_realistic_style_control=True, realistic_style_control=False, unwanted_mediums=False, 
                                 color_control=False, composition=True, 
                                 background_control=False, text_removal=True, 
                                 clothing_control=False, nsfw_filters=False, 
                                 violence_filters=False, strength_boost=False, 
                                 custom_negatives=""):
        
        # Set random seed for reproducible results
        if seed != 0:
            random.seed(seed)
        
        negatives = []
        enabled_categories = []
        
        # Add base categories based on toggles
        if base_quality:
            negatives.extend(self.generator.get_base_negatives())
            enabled_categories.append("Base Quality")
        
        # Build category list based on toggles
        categories = []
        if enhanced_quality:
            categories.append("enhanced_quality")
            enabled_categories.append("Enhanced Quality")
        if technical_artifacts:
            categories.append("technical")
            enabled_categories.append("Technical Artifacts")
        if anatomy_control:
            categories.append("anatomy")
            enabled_categories.append("Anatomy Control")
        if expression_control:
            categories.append("expressions")
            enabled_categories.append("Expression Control")
        if hair_control:
            categories.append("hair")
            enabled_categories.append("Hair Control")
        if non_realistic_style_control:
            categories.append("non_realistic_style_control")
            enabled_categories.append("Non-Realistic Style Control")
        if realistic_style_control:
            categories.append("realistic_style_control")
            enabled_categories.append("Realistic Style Control")
        if unwanted_mediums:
            categories.append("unwanted_mediums")
            enabled_categories.append("Unwanted Mediums")
        if color_control:
            categories.append("color_control")
            enabled_categories.append("Color Control")
        if composition:
            categories.append("composition")
            enabled_categories.append("Composition")
        if background_control:
            categories.append("background")
            enabled_categories.append("Background Control")
        if text_removal:
            categories.append("text_elements")
            enabled_categories.append("Text Removal")
        if clothing_control:
            categories.append("clothing")
            enabled_categories.append("Clothing Control")
        
        # Add category negatives
        if categories:
            negatives.extend(self.generator.get_category_negatives(categories))
        
        # Add optional filters
        if nsfw_filters:
            negatives.extend(self.generator.get_category_negatives(["nsfw_filters"]))
            enabled_categories.append("NSFW Filters")
        
        if violence_filters:
            negatives.extend(self.generator.get_category_negatives(["violence_filters"]))
            enabled_categories.append("Violence Filters")
        
        # Add custom negatives
        if custom_negatives.strip():
            custom_terms = [term.strip() for term in custom_negatives.split(",") if term.strip()]
            negatives.extend(custom_terms)
            enabled_categories.append(f"Custom ({len(custom_terms)} terms)")
        
        # Remove duplicates while preserving order
        seen = set()
        unique_negatives = []
        for negative in negatives:
            if negative not in seen:
                unique_negatives.append(negative)
                seen.add(negative)
        
        # Apply strength boost to critical terms
        if strength_boost:
            critical_terms = ["bad_anatomy", "bad_hands", "bad_face", "worst_quality", "low_quality"]
            boosted_negatives = []
            for negative in unique_negatives:
                if negative in critical_terms:
                    boosted_negatives.append(f"({negative}:1.2)")
                else:
                    boosted_negatives.append(negative)
            unique_negatives = boosted_negatives
            enabled_categories.append("Strength Boost")
        
        # Create category summary
        category_summary = ", ".join(enabled_categories) if enabled_categories else "No categories enabled"
        
        return (", ".join(unique_negatives), category_summary)


# Node registration
NODE_CLASS_MAPPINGS = {
    "FactoryPromptsNegative": PonyNegativeNode,
    "FactoryPromptsNegativeCategorized": PonyNegativeCategorizedNode,
    "FactoryPromptsNegativeToggle": PonyNegativeToggleNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FactoryPromptsNegative": "Factory Prompts Negative Generator",
    "FactoryPromptsNegativeCategorized": "Factory Prompts Negative (Categorized)",
    "FactoryPromptsNegativeToggle": "Factory Prompts Negative Generator (Toggles)"
}
