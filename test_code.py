from inference.engine import Model

ckpt_dir = "path_to_downloaded_model_directory"

ckpt_dir = "/home/sachin/code/dwani_org/new_translate/IndicTrans2/ckpoint/ct2-rotary-indictrans2-en-indic-dist-200M/en-indic-200m-ct2/ctranslate2_model"
model = Model(ckpt_dir, model_type="ctranslate2")

sents = ["This is a test sentence.", "Translate this too."]

# Batch translation
translations = model.batch_translate(sents, "eng_Latn", "hin_Deva")
print(translations)

# Paragraph translation
text = "This is a paragraph containing multiple sentences."
paragraph_translation = model.translate_paragraph(text, "eng_Latn", "hin_Deva")
print(paragraph_translation)
