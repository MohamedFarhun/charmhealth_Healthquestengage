/**
 * @license Copyright (c) 2003-2018, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	    // Define changes to default configuration here. For example:  

     config.language = 'en,ta,hi,fr,es,de,ar';  

    // config.uiColor = '#AADC6E';  

	config.language_list = [ 'ar:Arabic:rtl', 'en:English','fr:French', 'de:German', 'hi:Hindi', 'es:Spanish', 'ta:Tamil' ];

	/*config.toolbar = 'Cms';
    config.toolbar_Cms =
    [
        ['Source','-','Cut','Copy','Paste','PasteText','PasteFromWord','-','Undo','Redo','-','Bold','Italic','Underline','Strikethrough','Subscript','Superscript','-','CopyFormatting','RemoveFormat','-','Link','Unlink','-','Image','Table','SpecialChar','SpellCheck','magicline'],
        
    ];*/

    config.toolbar = [['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', 'Undo', 'Redo','Scayt','Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', 'CopyFormatting', 'RemoveFormat','Link', 'Unlink','Image', 'Table', 'HorizontalRule', 'SpecialChar','ckeditor_wiris_formulaEditor','ckeditor_wiris_formulaEditorChemistry']];

    config.disableNativeSpellChecker = false;
	
	config.extraPlugins = 'uploadimage,ckeditor_wiris';
	config.imageUploadUrl = '/uploader/upload.php?type=Images';
	config.filebrowserUploadMethod = 'form';
	
	config.allowedContent = true;
	//config.contentsCss = '/examnr/admin_assets/css/faculty-style.css';

    config.filebrowserBrowseUrl = '/examnr/templateEditor/kcfinder/browse.php?opener=ckeditor&type=files';

    config.filebrowserImageBrowseUrl = '/examnr/templateEditor/kcfinder/browse.php?opener=ckeditor&type=images';

    config.filebrowserFlashBrowseUrl = '/examnr/templateEditor/kcfinder/browse.php?opener=ckeditor&type=flash';

    config.filebrowserUploadUrl = '/examnr/templateEditor/kcfinder/upload.php?opener=ckeditor&type=files';

    config.filebrowserImageUploadUrl = '/examnr/templateEditor/kcfinder/upload.php?opener=ckeditor&type=images';

    config.filebrowserFlashUploadUrl = '/examnr/templateEditor/kcfinder/upload.php?opener=ckeditor&type=flash';

    config.removeButtons = 'Anchor,Underline,Strike,Subscript,Superscript';

    
};
