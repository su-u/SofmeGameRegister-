$('#js-selectFile').on('click', 'button', function () {
    $('#js-upload').click();
    return false;
});

$('#js-upload').on('change', function () {
    //�I�������t�@�C�������擾���ϐ��Ɋi�[
    var file = $(this).prop('files')[0];
    //�A�C�R����I�𒆂ɕύX
    $('#js-selectFile').find('.icon').addClass('select').html('�I��');
    //���I�����I���̏ꍇ�i.filename�����݂��Ȃ��ꍇ�j�̓t�@�C�����\���p��<div>�^�O��ǉ�
    if (!($('.filename').length)) {
        $('#js-selectFile').append('<div class="filename"></div>');
    };
    //�t�@�C������\��
    $('.filename').html('�t�@�C�����F' + file.name);
});