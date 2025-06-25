import unicodedata

def _get_char_effective_width(char):
    """
    使用 unicodedata 获取字符的等效显示宽度。
    返回 float：0.5 或 1.0
    """
    width = unicodedata.east_asian_width(char)

    if width in ('F', 'W'):
        return 2.0
    elif width in ('H', 'N', 'A'):
        return 1.0
    else:
        # Na（控制字符）或未知字符，默认设为 0.5
        return 1.0


def _get_text_effective_width(text):
    """
    返回一段文本的总等效显示宽度（以“汉字单位”为基准）
    """
    return sum(_get_char_effective_width(c) for c in text)


def _estimate_textbox_lines(x_in, font_size_pt, text):
    """
    根据给定文本内容估算所需文本框的内容行数。

    参数:
        x_in (float): 文本框宽度，单位英寸 (in)
        font_size_pt (int): 字号大小，单位磅 (pt)
        text (str): 要显示的文本内容（不含换行符）

    返回:
        int: 所需文本框高度（in）
    """
    char_count = _get_text_effective_width(text)
    x_pt = x_in * 72

    # 每个字符平均宽度约为字号的一半（适用于中文/英文混排）
    avg_char_width = font_size_pt / 2

    # 计算每行可容纳的字符数（向下取整）
    chars_per_line = int(x_pt // avg_char_width)

    if chars_per_line <= 0:
        raise ValueError("文本框过窄或字号过大，无法容纳任何字符")

    # 计算所需行数（向上取整）
    lines = (char_count + chars_per_line - 1) // chars_per_line
    return lines


def estimate_textbox_height(x_in, font_size_pt, text):
    res = _estimate_textbox_lines(x_in, font_size_pt, text)
    if font_size_pt == 32:
        return res * 0.5393 + 0.098425
    elif font_size_pt == 18:
        return res * 0.3031 + 0.102362
    elif font_size_pt == 24:
        return res * 0.4055 + 0.098425
    else:
        return _estimate_textbox_lines(x_in, font_size_pt, text) * 2
#//32，0.25+1.37lcm// 18，0.26+0.77l cm //24，0.25+1.03l cm