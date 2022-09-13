function upvote_downvote_fun(question_id, vote_type){
  $.ajax({
      data:{
        'question_id' : question_id,
        'vote_type' : vote_type
      },
      url: "/like_question/",
      type: "GET",
      success: function(response) {
        document.getElementById("question_vote_" + question_id).innerHTML = response.total_votes
      }
    });
  }
function upvote_downvote_fun1(answer_id, vote_type){

  $.ajax({
      data:{
        'answer_id' : answer_id,
        'vote_type' : vote_type
      },
      url: "/like_answer/",
      type: "GET",
      success: function(response) {
        document.getElementById("answer_vote_" + answer_id).innerHTML = response.total_votes
      }
    });
  }
function comment_fun(question_id){
  var cmnt_body = document.getElementById("cmnt_" + question_id + "_body").value
  if (cmnt_body.length > 0){
    $.ajax({
        data:{
            'question_id' : question_id,
            'cmnt_body' : cmnt_body
      },
      url: "/question-comment/",
      type: "GET",
      success: function(response) {
        location.reload();
        document.getElementById("cmnt_username_" + question_id).innerHTML = response.cmnt_username + "(" + response.cmnt_add_time + ")"
        document.getElementById("cmnt_body_" + question_id).innerHTML = response.cmnt_body
      }
    });
  }
}


function comment_fun1(answer_id){
  var cmnt_body = document.getElementById("cmnt_" + answer_id + "_body").value
  if (cmnt_body.length > 0){
    $.ajax({
        data:{
            'answer_id' : answer_id,
            'cmnt_body' : cmnt_body
      },
      url: "/answer-comment/",
      type: "GET",
      success: function(response) {
        location.reload();
        document.getElementById("cmnt_username_" + answer_id).innerHTML = response.cmnt_username + "(" + response.cmnt_add_time + ")"
        document.getElementById("cmnt_body_" + answer_id).innerHTML = response.cmnt_body
      }
    });
  }
}
