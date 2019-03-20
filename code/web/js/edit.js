function outputData(data) {
    //显示输出
    var outputtime = moment().format('MMMM Do YYYY, h:mm:ss a');
    var line = '-------------------------------------------------------------------';
    $("#output").empty();
    $("#output").append(outputtime + '<br>' + line + '<br>' + data);
}

function getResult(code) {
    //获取代码执行结果
    outputData('代码正在执行中，请稍后...')
    pack = {
        'code' : code,
    }
    var server_url = location.protocol + '//' + document.domain + ':5000'
    $.post( server_url, JSON.stringify(pack), function(data) {
        console.log(data)
        console.log(data['errors'].length)
        if (data['output'].length != 0) {
            outputData(data['output']);
            console.log('success');
        } else {
            outputData(data['errors']);
            console.log('error');
        }
    });

}
