'''
     
    
    Main Purpose:
    => Define a custom component for text styling.
'''
from app import (
    ft
)
from app.style import *
from typing import List, Dict, Any, Tuple, Union, Optional
from flet import TextSpan, TextOverflow



class TextCustom(ft.Text):
    '''
        - Inherits from: ft.Text
        - Purpose: Define a custom component for text styling.
    '''
    def __init__(self, 
                 value: Optional[str] = None, 
                 spans: Optional[List[TextSpan]] = None, 
                 text_align: Optional[ft.TextAlign] = None, 
                 font_family: Optional[str] = None, 
                 size: Optional[Union[int, float]] = None, 
                 weight: Optional[ft.FontWeight] = None, 
                 italic: Optional[bool] = None, 
                 style: Optional[Union[ft.TextThemeStyle, ft.TextStyle]] = None, 
                 theme_style: Optional[ft.TextThemeStyle] = None, 
                 max_lines: Optional[int] = None, 
                 overflow: ft.TextOverflow = TextOverflow.NONE, 
                 selectable: Optional[bool] = None, 
                 no_wrap: Optional[bool] = None, 
                 color: Optional[str] = None, 
                 bgcolor: Optional[str] = None, 
                 semantics_label: Optional[str] = None, 
                 ref: Optional[ft.Ref] = None, 
                 key: Optional[str] = None, 
                 width: Optional[Union[int, float]] = None, 
                 height: Optional[Union[int, float]] = None, 
                 left: Optional[Union[int, float]] = None, 
                 top: Optional[Union[int, float]] = None, 
                 right: Optional[Union[int, float]] = None, 
                 bottom: Optional[Union[int, float]] = None, 
                 expand: Optional[Union[bool, int]] = None, 
                 expand_loose: Optional[bool] = None, 
                 col: Optional[Union[Dict[str, Union[int, float]], int, float]] = None, 
                 opacity: Optional[Union[int, float]] = None, 
                 rotate: Optional[Union[int, float, ft.Rotate]] = None, 
                 scale: Optional[Union[int, float, ft.Scale]] = None, 
                 offset: Optional[Union[ft.Offset, Tuple[Union[float, int], Union[float, int]]]] = None, 
                 aspect_ratio: Optional[Union[int, float]] = None, 
                 animate_opacity: Optional[Union[bool, int, ft.Animation]] = None, 
                 animate_size: Optional[Union[bool, int, ft.Animation]] = None, 
                 animate_position: Optional[Union[bool, int, ft.Animation]] = None, 
                 animate_rotation: Optional[Union[bool, int, ft.Animation]] = None, 
                 animate_scale: Optional[Union[bool, int, ft.Animation]] = None, 
                 animate_offset: Optional[Union[bool, int, ft.Animation]] = None, 
                 on_animation_end=None, 
                 tooltip: Optional[str] = None, 
                 visible: Optional[bool] = None, 
                 disabled: Optional[bool] = None, 
                 data: Any = None, 
                 rtl: Optional[bool] = None):
        super().__init__(value, spans, text_align, font_family, size, weight, italic, style, theme_style, max_lines, overflow, selectable, no_wrap, color, bgcolor, semantics_label, ref, key, width, height, left, top, right, bottom, expand, expand_loose, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, tooltip, visible, disabled, data, rtl)
        
        