from utilities import *

def markdown_to_blocks(markdown_text):
    blocks = []
    if markdown_text == "" or markdown_text is None:
        return markdown_text
    
    lines = markdown_text.split("\n")
    
    # probably a fancier way to do this but this works ¯\_(ツ)_/¯
    start = 0
    end = 0
    prev_empty = 0
    prev_not_empty = 0
    inside_text_block = False
    if lines:
        for i in range(0, len(lines)):
            line = lines[i]
            # empty line is not saved
            if line == "" or line == None:
                prev_empty = i
            else:
                prev_not_empty = i
            # check beginning of new text block
            if prev_empty < prev_not_empty:
                # if inside a text block then continue to the next line
                if not inside_text_block:
                    inside_text_block = True
                    start = i
            # check for end of the current text block
            elif prev_empty > prev_not_empty:
                # a new blank line was found so we need to snapshot the text block
                end = i
                block = lines[start:end]
                blocks.append("\n".join(block))
                inside_text_block = False
    return blocks