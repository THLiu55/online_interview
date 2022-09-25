document.addEventListener('DOMContentLoaded', function () {
  var modeSwitch = document.querySelector('.mode-switch');

  modeSwitch.addEventListener('click', function () {                     document.documentElement.classList.toggle('dark');
    modeSwitch.classList.toggle('active');
  });
  
  var listView = document.querySelector('.list-view');
  var gridView = document.querySelector('.grid-view');
  var projectsList = document.querySelector('.project-boxes');
  
  listView.addEventListener('click', function () {
    gridView.classList.remove('active');
    listView.classList.add('active');
    projectsList.classList.remove('jsGridView');
    projectsList.classList.add('jsListView');
  });
  
  gridView.addEventListener('click', function () {
    gridView.classList.add('active');
    listView.classList.remove('active');
    projectsList.classList.remove('jsListView');
    projectsList.classList.add('jsGridView');
  });
  
  document.querySelector('.messages-btn').addEventListener('click', function () {
    document.querySelector('.messages-section').classList.add('show');
  });
  
  document.querySelector('.messages-close').addEventListener('click', function() {
    document.querySelector('.messages-section').classList.remove('show');
  });
});
function btnupcoming() {
  document.getElementById('now').classList.add('active');
  document.getElementById('ed').classList.remove('active');

  document.getElementById('uncomingevents').style.display = 'flex';
  document.getElementById('finishedevents').style.display = 'none';
}

function btnfinished() {
  document.getElementById('ed').classList.add('active');
  document.getElementById('now').classList.remove('active');

  document.getElementById('uncomingevents').style.display = 'none';
  document.getElementById('finishedevents').style.display = 'flex';
}
