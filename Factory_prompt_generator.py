#!/usr/bin/env python3

"""
Factory Prompt Generator - JSON-Based Tag Accumulator (SFW Version)
Loads tags from external JSON file for better organization
Separates body features and color options
Works with all checkpoint types (Pony, SDXL, SD1.5, etc.)
GitHub-compliant SFW content only
"""

import json
import os
import random

class FactoryPromptsPositiveNode:
    """
    A streamlined node that uses JSON-based tags and accumulates selections into a prompt.
    Features separated body types and clothing color options.
    Works with all checkpoint types.
    """
    
    def __init__(self):
        # Load tags from JSON file
        self.tags = self.load_tags()
    
    def load_tags(self):
        """Load tag data from JSON file"""
        try:
            json_path = os.path.join(os.path.dirname(__file__), "factory_tags.json")
            with open(json_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading tags JSON: {e}")
            return {}
    
    def create_dropdown_options(self, tag_list):
        """Create dropdown options with random + tags (SFW only, no 'none' option)"""
        options = ["random"] + tag_list
        return options
    
    @classmethod
    def INPUT_TYPES(cls):
        # Create instance to access tags
        instance = cls()
        tags = instance.tags
        
        return {
            "required": {
                "quality_level": (["high", "medium", "varied"], {"default": "high"}),
                "source_style": (["anime", "cartoon", "realistic", "photorealistic", "furry", "mixed"], {"default": "anime"}),
                "character_count": (["1girl", "1boy", "2girls", "2boys", "1girl_1boy", "3girls", "3boys", "2girls_1boy", "1girl_2boys", "4girls", "4boys", "5girls", "5boys", "6+girls", "6+boys", "multiple_girls", "multiple_boys", "crowd"], {"default": "1girl"}),
                "character_preference": (["single", "couple", "group", "crowd"], {"default": "single"}),
                "clothing_style": (["school", "casual", "formal", "traditional", "fantasy", "mixed"], {"default": "casual"}),
                "location_type": (["indoor", "outdoor", "mixed"], {"default": "indoor"}),
                "include_artist": ("BOOLEAN", {"default": True}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
            "optional": {
                # Character Features
                "hair_color": (instance.create_dropdown_options(tags.get("character_features", {}).get("hair_colors", [])), {"default": "random"}),
                "hair_length": (instance.create_dropdown_options(tags.get("character_features", {}).get("hair_lengths", [])), {"default": "random"}),
                "hair_style": (instance.create_dropdown_options(tags.get("character_features", {}).get("hair_styles", [])), {"default": "random"}),
                "eye_color": (instance.create_dropdown_options(tags.get("character_features", {}).get("eye_colors", [])), {"default": "random"}),
                "skin_color": (instance.create_dropdown_options(tags.get("character_features", {}).get("skin_colors", [])), {"default": "random"}),
                "expression": (instance.create_dropdown_options(
                    tags.get("character_features", {}).get("expressions", [])
                ), {"default": "random"}),
                
                # Separated Body Features
                "body_type": (instance.create_dropdown_options(tags.get("body_features", {}).get("body_types", [])), {"default": "random"}),
                "chest_type": (instance.create_dropdown_options(
                    tags.get("body_features", {}).get("chest_types", [])
                ), {"default": "random"}),
                "hip_type": (instance.create_dropdown_options(
                    tags.get("body_features", {}).get("hip_types", [])
                ), {"default": "random"}),
                "leg_type": (instance.create_dropdown_options(
                    tags.get("body_features", {}).get("leg_types", [])
                ), {"default": "random"}),
                
                # SFW Poses only
                "pose": (instance.create_dropdown_options(
                    tags.get("poses", [])
                ), {"default": "random"}),
                
                # Multi-Character Position System (SFW only)
                "multi_char_position": (instance.create_dropdown_options(
                    tags.get("multi_character_positions", {}).get("two_character", {}).get("casual", []) +
                    tags.get("multi_character_positions", {}).get("two_character", {}).get("friendly", []) +
                    tags.get("multi_character_positions", {}).get("two_character", {}).get("romantic", []) +
                    tags.get("multi_character_positions", {}).get("three_character", {}).get("casual", []) +
                    tags.get("multi_character_positions", {}).get("three_character", {}).get("friendly", []) +
                    tags.get("multi_character_positions", {}).get("group_character", {}).get("social", []) +
                    tags.get("multi_character_positions", {}).get("group_character", {}).get("collaborative", [])
                ), {"default": "random"}),
                
                # Individual Character Actions (SFW only)
                "character_1_action": (instance.create_dropdown_options(
                    tags.get("individual_actions", {}).get("character_1", [])
                ), {"default": "random"}),
                "character_2_action": (instance.create_dropdown_options(
                    tags.get("individual_actions", {}).get("character_2", [])
                ), {"default": "random"}),
                "character_3_action": (instance.create_dropdown_options(
                    tags.get("individual_actions", {}).get("character_3", [])
                ), {"default": "random"}),
                
                # Camera and Composition
                "camera_shot": (instance.create_dropdown_options(tags.get("technical", {}).get("camera_shots", [])), {"default": "random"}),
                
                # Locations
                "indoor_location": (instance.create_dropdown_options(tags.get("environments", {}).get("indoor", [])), {"default": "random"}),
                "outdoor_location": (instance.create_dropdown_options(tags.get("environments", {}).get("outdoor", [])), {"default": "random"}),
                "fantasy_location": (instance.create_dropdown_options(tags.get("environments", {}).get("fantasy", [])), {"default": "random"}),
                
                # Artistic Elements
                "lighting": (instance.create_dropdown_options(tags.get("lighting", [])), {"default": "random"}),
                "emotion": (instance.create_dropdown_options(tags.get("emotions", [])), {"default": "random"}),
                
                # Clothing Categories (SFW only)
                "school_uniform_top": (instance.create_dropdown_options(
                    tags.get("clothing", {}).get("school_uniform", {}).get("tops", [])
                ), {"default": "random"}),
                "school_uniform_bottom": (instance.create_dropdown_options(
                    tags.get("clothing", {}).get("school_uniform", {}).get("bottoms", [])
                ), {"default": "random"}),
                "school_uniform_footwear": (instance.create_dropdown_options(
                    tags.get("clothing", {}).get("school_uniform", {}).get("footwear", [])
                ), {"default": "random"}),
                
                "casual_top": (instance.create_dropdown_options(
                    tags.get("clothing", {}).get("casual", {}).get("tops", [])
                ), {"default": "random"}),
                "casual_bottom": (instance.create_dropdown_options(
                    tags.get("clothing", {}).get("casual", {}).get("bottoms", [])
                ), {"default": "random"}),
                "casual_dress": (instance.create_dropdown_options(
                    tags.get("clothing", {}).get("casual", {}).get("dresses", [])
                ), {"default": "random"}),
                
                "formal_top": (instance.create_dropdown_options(
                    tags.get("clothing", {}).get("formal", {}).get("tops", [])
                ), {"default": "random"}),
                "formal_bottom": (instance.create_dropdown_options(
                    tags.get("clothing", {}).get("formal", {}).get("bottoms", [])
                ), {"default": "random"}),
                "formal_dress": (instance.create_dropdown_options(
                    tags.get("clothing", {}).get("formal", {}).get("dresses", [])
                ), {"default": "random"}),
                
                "accessories": (instance.create_dropdown_options(
                    tags.get("clothing", {}).get("accessories", [])
                ), {"default": "random"}),
                
                "underwear_top": (instance.create_dropdown_options(
                    tags.get("clothing", {}).get("underwear", {}).get("tops", {}).get("items", [])
                ), {"default": "random"}),
                "underwear_top_color": (instance.create_dropdown_options(tags.get("clothing", {}).get("underwear", {}).get("tops", {}).get("colors", [])), {"default": "random"}),
                "underwear_bottom": (instance.create_dropdown_options(
                    tags.get("clothing", {}).get("underwear", {}).get("bottoms", {}).get("items", [])
                ), {"default": "random"}),
                "underwear_bottom_color": (instance.create_dropdown_options(tags.get("clothing", {}).get("underwear", {}).get("bottoms", {}).get("colors", [])), {"default": "random"}),
                
                # Technical Settings
                "quality": (instance.create_dropdown_options(tags.get("technical", {}).get("quality", [])), {"default": "random"}),
                "composition": (instance.create_dropdown_options(tags.get("technical", {}).get("composition", [])), {"default": "random"}),
                "color_scheme": (instance.create_dropdown_options(tags.get("technical", {}).get("color_schemes", [])), {"default": "random"}),
                "time_period": (instance.create_dropdown_options(tags.get("technical", {}).get("time_periods", [])), {"default": "random"}),
                "weather": (instance.create_dropdown_options(tags.get("technical", {}).get("weather", [])), {"default": "random"}),
                "special_effects": (instance.create_dropdown_options(tags.get("technical", {}).get("special_effects", [])), {"default": "random"}),
                "image_style": (instance.create_dropdown_options(tags.get("technical", {}).get("image_styles", [])), {"default": "random"}),
                
                # Emphasis Controls - Add weight to specific categories
                "character_emphasis": (["low", "medium", "high", "very_high"], {"default": "medium"}),
                "pose_emphasis": (["low", "medium", "high", "very_high"], {"default": "medium"}),
                "clothing_emphasis": (["low", "medium", "high", "very_high"], {"default": "medium"}),
                "location_emphasis": (["low", "medium", "high", "very_high"], {"default": "medium"}),
                "art_style_emphasis": (["low", "medium", "high", "very_high"], {"default": "medium"}),
                
                "custom_elements": ("STRING", {"multiline": True, "default": ""}),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "selection_summary")
    FUNCTION = "generate_prompts"
    CATEGORY = "Prompt Factory"
    
    def apply_emphasis(self, tag, emphasis_level):
        """Apply emphasis brackets to a tag based on emphasis level"""
        if not tag:
            return tag
        elif emphasis_level == "low":
            return f"({tag})"
        elif emphasis_level == "high":
            return f"(({tag}))"
        elif emphasis_level == "very_high":
            return f"((({tag})))"
        else:  # medium or any other value
            return tag
    
    def add_tag(self, tag, category_name, random_choices=None, prompt_parts=None, selected_tags=None, emphasis_level="medium"):
        """Helper function to add tags with proper handling (SFW only)"""
        if prompt_parts is None:
            prompt_parts = []
        if selected_tags is None:
            selected_tags = []
            
        if tag == "random" and random_choices:
            # For SFW version, use only the main list
            if isinstance(random_choices, list):
                all_choices = random_choices
            else:
                all_choices = random_choices
                
            if all_choices:
                chosen_tag = random.choice(all_choices)
                emphasized_tag = self.apply_emphasis(chosen_tag, emphasis_level)
                prompt_parts.append(emphasized_tag)
                selected_tags.append(f"{category_name}: {chosen_tag} (random)" + (f" [emphasized: {emphasis_level}]" if emphasis_level != "medium" else ""))
        else:
            emphasized_tag = self.apply_emphasis(tag, emphasis_level)
            prompt_parts.append(emphasized_tag)
            selected_tags.append(f"{category_name}: {tag}" + (f" [emphasized: {emphasis_level}]" if emphasis_level != "medium" else ""))
    
    def generate_prompts(self, quality_level, source_style, character_count, character_preference, 
                        clothing_style, location_type, include_artist, seed, **kwargs):
        
        # Set random seed for reproducible results
        if seed != 0:
            random.seed(seed)
        
        prompt_parts = []
        selected_tags = []  # To track what was selected for user feedback
        
        # Extract emphasis levels from kwargs
        character_emphasis = kwargs.get("character_emphasis", "medium")
        pose_emphasis = kwargs.get("pose_emphasis", "medium")
        clothing_emphasis = kwargs.get("clothing_emphasis", "medium")
        location_emphasis = kwargs.get("location_emphasis", "medium")
        art_style_emphasis = kwargs.get("art_style_emphasis", "medium")
        
        # Add quality tags based on level (always included)
        if quality_level == "high":
            prompt_parts.extend(["masterpiece", "best_quality", "high_quality"])
            selected_tags.append("Quality Level: high (masterpiece, best_quality, high_quality)")
        elif quality_level == "medium":
            prompt_parts.extend(["best_quality", "high_quality"])
            selected_tags.append("Quality Level: medium (best_quality, high_quality)")
        elif quality_level == "varied":
            quality_choice = random.choice(["masterpiece", "best_quality", "high_quality", "normal_quality"])
            prompt_parts.append(quality_choice)
            selected_tags.append(f"Quality Level: varied ({quality_choice})")
        
        # Required parameters - always add since "none" option removed
        source_map = {
            "anime": "source_anime",
            "cartoon": "source_cartoon", 
            "realistic": "source_realistic",
            "photorealistic": "source_pony",
            "furry": "source_furry",
            "mixed": "source_anime"
        }
        if source_style in source_map:
            prompt_parts.append(source_map[source_style])
            selected_tags.append(f"Source Style: {source_style}")
        
        prompt_parts.append(character_count)
        selected_tags.append(f"Character Count: {character_count}")
        
        # Process all optional parameters
        for param_name, param_value in kwargs.items():
                
            # Handle clothing color pairs for tops and bottoms
            if param_name.endswith("_color"):
                clothing_item = param_name.replace("_color", "")
                if clothing_item in kwargs:
                    # Handle accessories color separately
                    if clothing_item == "accessories":
                        self.add_tag(param_value, "Accessories Color", 
                                   self.tags.get("clothing", {}).get("accessories", {}).get("colors", []),
                                   prompt_parts, selected_tags, clothing_emphasis)
                        continue
                    
                    # Extract category and type (top/bottom)
                    if "_top" in clothing_item:
                        category = clothing_item.replace("_top", "")
                        item_type = "tops"
                    elif "_bottom" in clothing_item:
                        category = clothing_item.replace("_bottom", "")
                        item_type = "bottoms"
                    else:
                        continue
                    
                    # Only add color if the clothing item was also selected
                    self.add_tag(param_value, f"{clothing_item.replace('_', ' ').title()} Color", 
                               self.tags.get("clothing", {}).get(category, {}).get(item_type, {}).get("colors", []),
                               prompt_parts, selected_tags, clothing_emphasis)
                continue
            
            # Handle regular parameters
            if param_name in ["hair_color", "hair_length", "hair_style", "eye_color", "skin_color"]:
                self.add_tag(param_value, param_name.replace("_", " ").title(),
                           self.tags.get("character_features", {}).get(param_name.replace("_", "_") + "s", []),
                           prompt_parts, selected_tags, character_emphasis)
            
            elif param_name == "expression":
                self.add_tag(param_value, "Expression",
                           self.tags.get("character_features", {}).get("expressions", {}),
                           prompt_parts, selected_tags, character_emphasis)
            
            elif param_name in ["body_type", "chest_type", "hip_type", "leg_type"]:
                self.add_tag(param_value, param_name.replace("_", " ").title(),
                           self.tags.get("body_features", {}).get(param_name + "s", {}),
                           prompt_parts, selected_tags, character_emphasis)
            
            elif param_name == "pose":
                # Handle SFW poses only
                self.add_tag(param_value, "Pose",
                           self.tags.get("poses", []),
                           prompt_parts, selected_tags, pose_emphasis)
            
            elif param_name == "multi_char_position":
                # Handle multi-character positions
                # Check which category this position belongs to and add appropriate logic
                multi_char_tags = self.tags.get("multi_character_positions", {})
                
                # Check all categories to find where this position belongs
                found_position = False
                for char_count in ["two_character", "three_character", "group_character"]:
                    for mood_type in ["casual", "friendly", "romantic", "social", "collaborative"]:
                        positions = multi_char_tags.get(char_count, {}).get(mood_type, [])
                        if param_value in positions or param_value == "random":
                                if param_value == "random":
                                    # For random, use only SFW positions
                                    all_positions = []
                                    for ct in ["two_character", "three_character", "group_character"]:
                                        for mt in ["casual", "friendly", "romantic", "social", "collaborative"]:
                                            all_positions.extend(multi_char_tags.get(ct, {}).get(mt, []))
                                    
                                    if all_positions:
                                        chosen_position = random.choice(all_positions)
                                        prompt_parts.append(chosen_position)
                                        selected_tags.append(f"Multi-Character Position: {chosen_position} (random)")
                                else:
                                    prompt_parts.append(param_value)
                                    selected_tags.append(f"Multi-Character Position: {param_value}")
                                found_position = True
                                break
                        if found_position:
                            break
            
            elif param_name in ["character_1_action", "character_2_action", "character_3_action"]:
                # Handle individual character actions
                char_num = param_name.split("_")[1]
                self.add_tag(param_value, f"Character {char_num} Action",
                           self.tags.get("individual_actions", {}).get(f"character_{char_num}", {}),
                           prompt_parts, selected_tags, pose_emphasis)
            
            elif param_name in ["indoor_location", "outdoor_location"]:
                location_key = param_name.split("_")[0]
                self.add_tag(param_value, param_name.replace("_", " ").title(),
                           self.tags.get("locations", {}).get(location_key, []),
                           prompt_parts, selected_tags, location_emphasis)
            
            elif param_name in ["camera_shot", "art_style", "lighting"]:
                tech_key = param_name + "s" if not param_name.endswith("s") else param_name
                self.add_tag(param_value, param_name.replace("_", " ").title(),
                           self.tags.get("technical", {}).get(tech_key, []),
                           prompt_parts, selected_tags, art_style_emphasis)
            
            elif param_name == "artist_style" and include_artist:
                self.add_tag(param_value, "Artist Style",
                           self.tags.get("artists", []),
                           prompt_parts, selected_tags, art_style_emphasis)
            
            # Handle clothing items with new top/bottom structure
            elif ("_top" in param_name or "_bottom" in param_name) and not param_name.endswith("_color"):
                # Extract category and type (top/bottom)
                if "_top" in param_name:
                    category = param_name.replace("_top", "")
                    item_type = "tops"
                elif "_bottom" in param_name:
                    category = param_name.replace("_bottom", "")
                    item_type = "bottoms"
                
                if category in ["school_uniform", "casual_wear", "formal_wear", "traditional_wear", 
                              "fantasy_wear", "swimwear", "sports_wear", "underwear"]:
                    self.add_tag(param_value, param_name.replace("_", " ").title(),
                               self.tags.get("clothing", {}).get(category, {}).get(item_type, {}),
                               prompt_parts, selected_tags, clothing_emphasis)
            
            # Handle accessories (still uses old structure)
            elif param_name == "accessories":
                self.add_tag(param_value, "Accessories",
                           self.tags.get("clothing", {}).get("accessories", {}),
                           prompt_parts, selected_tags, clothing_emphasis)
            
            elif param_name in ["quality", "composition", "color_scheme", "time_period", 
                              "weather", "special_effects", "image_style"]:
                tech_key = param_name + "s" if param_name in ["quality", "composition"] else param_name.replace("_", "_") + "s"
                self.add_tag(param_value, param_name.replace("_", " ").title(),
                           self.tags.get("technical", {}).get(tech_key, []),
                           prompt_parts, selected_tags, art_style_emphasis)
        
        # Add custom elements if provided
        custom_elements = kwargs.get("custom_elements", "")
        if custom_elements and custom_elements.strip():
            custom_list = [elem.strip() for elem in custom_elements.split(',') if elem.strip()]
            prompt_parts.extend(custom_list)
            selected_tags.append(f"Custom Elements: {', '.join(custom_list)}")
        
        # Join everything
        positive_prompt = ", ".join(prompt_parts)
        
        # Create summary of selections for user feedback
        selections_summary = "\n".join(selected_tags)
        
        # Return positive prompt and selection summary
        return (positive_prompt, selections_summary)


# Node registration
NODE_CLASS_MAPPINGS = {
    "FactoryPromptsPositive": FactoryPromptsPositiveNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FactoryPromptsPositive": "Factory Prompts Generator (Positive)"
}
