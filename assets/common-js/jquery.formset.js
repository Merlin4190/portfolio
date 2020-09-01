function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+)');
    var replacement = prefix + '-' + ndx;
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}
function cloneMore(selector, prefix) {
    var prefix = 'portfolios';
    var newElement = $(selector).clone(true);
    var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
    newElement.find(':input:not([type=button]):not([type=submit]):not([type=reset])').each(function() {
        var name = $(this).attr('name')
        if(name) {
            name = name.replace('-' + (total-1) + '-', '-' + total + '-');
            var id = 'id_' + name;
            $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
        }
    });
    newElement.find('label').each(function() {
        var forValue = $(this).attr('for');
        if (forValue) {
          forValue = forValue.replace('-' + (total-1) + '-', '-' + total + '-');
          $(this).attr({'for': forValue});
        }
    });
    total++;
    $('#id_' + prefix + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
    var conditionRow = $('.form-row:not(:last)');
    conditionRow.find('.btn.add-form-row')
    .removeClass('btn-success').addClass('btn-danger')
    .removeClass('add-form-row').addClass('remove-form-row')
    .html('<i class="icon trash ion-ios-trash"></i> Remove');
    return false;
}
function cloneMore1(selector, prefix) {
    var prefix = 'experiences';
    var newElement = $(selector).clone(true);
    var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
    newElement.find(':input:not([type=button]):not([type=submit]):not([type=reset])').each(function() {
        var name = $(this).attr('name')
        if(name) {
            name = name.replace('-' + (total-1) + '-', '-' + total + '-');
            var id = 'id_' + name;
            $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
        }
    });
    newElement.find('label').each(function() {
        var forValue = $(this).attr('for');
        if (forValue) {
          forValue = forValue.replace('-' + (total-1) + '-', '-' + total + '-');
          $(this).attr({'for': forValue});
        }
    });
    total++;
    $('#id_' + prefix + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
    var conditionRow = $('.form-row1:not(:last)');
    conditionRow.find('.btn.add-form-row1')
    .removeClass('btn-success').addClass('btn-danger')
    .removeClass('add-form-row1').addClass('remove-form-row1')
    .html('<i class="icon trash ion-ios-trash"></i> Remove');
    return false;
}
function cloneMore2(selector, prefix) {
    var prefix = 'educations';
    var newElement = $(selector).clone(true);
    var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
    newElement.find(':input:not([type=button]):not([type=submit]):not([type=reset])').each(function() {
        var name = $(this).attr('name')
        if(name) {
            name = name.replace('-' + (total-1) + '-', '-' + total + '-');
            var id = 'id_' + name;
            $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
        }
    });
    newElement.find('label').each(function() {
        var forValue = $(this).attr('for');
        if (forValue) {
          forValue = forValue.replace('-' + (total-1) + '-', '-' + total + '-');
          $(this).attr({'for': forValue});
        }
    });
    total++;
    $('#id_' + prefix + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
    var conditionRow = $('.form-row2:not(:last)');
    conditionRow.find('.btn.add-form-row2')
    .removeClass('btn-success').addClass('btn-danger')
    .removeClass('add-form-row2').addClass('remove-form-row2')
    .html('<i class="icon trash ion-ios-trash"></i> Remove');
    return false;
}
function cloneMore3(selector, prefix) {
    var prefix = 'achievements';
    var newElement = $(selector).clone(true);
    var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
    newElement.find(':input:not([type=button]):not([type=submit]):not([type=reset])').each(function() {
        var name = $(this).attr('name')
        if(name) {
            name = name.replace('-' + (total-1) + '-', '-' + total + '-');
            var id = 'id_' + name;
            $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
        }
    });
    newElement.find('label').each(function() {
        var forValue = $(this).attr('for');
        if (forValue) {
          forValue = forValue.replace('-' + (total-1) + '-', '-' + total + '-');
          $(this).attr({'for': forValue});
        }
    });
    total++;
    $('#id_' + prefix + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
    var conditionRow = $('.form-row3:not(:last)');
    conditionRow.find('.btn.add-form-row3')
    .removeClass('btn-success').addClass('btn-danger')
    .removeClass('add-form-row3').addClass('remove-form-row3')
    .html('<i class="icon trash ion-ios-trash"></i> Remove');
    return false;
}
function cloneMore4(selector, prefix) {
  var prefix = 'skills';
  var newElement = $(selector).clone(true);
  var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
  newElement.find(':input:not([type=button]):not([type=submit]):not([type=reset])').each(function() {
      var name = $(this).attr('name')
      if(name) {
          name = name.replace('-' + (total-1) + '-', '-' + total + '-');
          var id = 'id_' + name;
          $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
      }
  });
  newElement.find('label').each(function() {
      var forValue = $(this).attr('for');
      if (forValue) {
        forValue = forValue.replace('-' + (total-1) + '-', '-' + total + '-');
        $(this).attr({'for': forValue});
      }
  });
  total++;
  $('#id_' + prefix + '-TOTAL_FORMS').val(total);
  $(selector).after(newElement);
  var conditionRow = $('.form-row4:not(:last)');
  conditionRow.find('.btn.add-form-row4')
  .removeClass('btn-success').addClass('btn-danger')
  .removeClass('add-form-row4').addClass('remove-form-row4')
  .html('<i class="icon trash ion-ios-trash"></i> Remove');
  return false;
}

function deleteForm(prefix, btn) {
    var prefix = 'portfolios';
    var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    if (total > 1){
        btn.closest('.form-row').remove();
        var forms = $('.form-row');
        $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
        for (var i=0, formCount=forms.length; i<formCount; i++) {
            $(forms.get(i)).find(':input').each(function() {
                updateElementIndex(this, prefix, i);
            });
        }
    }
    return false;
}
function deleteForm1(prefix, btn) {
    var prefix = 'experiences';
    var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    if (total > 1){
        btn.closest('.form-row1').remove();
        var forms = $('.form-row1');
        $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
        for (var i=0, formCount=forms.length; i<formCount; i++) {
            $(forms.get(i)).find(':input').each(function() {
                updateElementIndex(this, prefix, i);
            });
        }
    }
    return false;
}
function deleteForm2(prefix, btn) {
    var prefix = 'educations';
    var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    if (total > 1){
        btn.closest('.form-row2').remove();
        var forms = $('.form-row2');
        $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
        for (var i=0, formCount=forms.length; i<formCount; i++) {
            $(forms.get(i)).find(':input').each(function() {
                updateElementIndex(this, prefix, i);
            });
        }
    }
    return false;
}
function deleteForm3(prefix, btn) {
    var prefix = 'achievements';
    var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    if (total > 1){
        btn.closest('.form-row3').remove();
        var forms = $('.form-row3');
        $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
        for (var i=0, formCount=forms.length; i<formCount; i++) {
            $(forms.get(i)).find(':input').each(function() {
                updateElementIndex(this, prefix, i);
            });
        }
    }
    return false;
}
function deleteForm4(prefix, btn) {
  var prefix = 'skills';
  var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
  if (total > 1){
      btn.closest('.form-row4').remove();
      var forms = $('.form-row4');
      $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
      for (var i=0, formCount=forms.length; i<formCount; i++) {
          $(forms.get(i)).find(':input').each(function() {
              updateElementIndex(this, prefix, i);
          });
      }
  }
  return false;
}

$(document).on('click', '.add-form-row', function(e){
    e.preventDefault();
    cloneMore('.form-row:last', 'form');
    return false;
});
$(document).on('click', '.remove-form-row', function(e){
    e.preventDefault();
    deleteForm('form', $(this));
    return false;
});

$(document).on('click', '.add-form-row1', function(e){
    e.preventDefault();
    cloneMore1('.form-row1:last', 'form');
    return false;
});
$(document).on('click', '.remove-form-row1', function(e){
    e.preventDefault();
    deleteForm1('form', $(this));
    return false;
});

$(document).on('click', '.add-form-row2', function(e){
    e.preventDefault();
    cloneMore2('.form-row2:last', 'form');
    return false;
});
$(document).on('click', '.remove-form-row2', function(e){
    e.preventDefault();
    deleteForm2('form', $(this));
    return false;
});

$(document).on('click', '.add-form-row3', function(e){
    e.preventDefault();
    cloneMore3('.form-row3:last', 'form');
    return false;
});
$(document).on('click', '.remove-form-row3', function(e){
    e.preventDefault();
    deleteForm3('form', $(this));
    return false;
});

$(document).on('click', '.add-form-row4', function(e){
    e.preventDefault();
    cloneMore4('.form-row4:last', 'form');
    return false;
});
$(document).on('click', '.remove-form-row4', function(e){
    e.preventDefault();
    deleteForm4('form', $(this));
    return false;
});