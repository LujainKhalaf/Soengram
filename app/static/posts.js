async function deletePost(e) {
    const postId = await e.getAttribute('data-post-id');
    const formData = new FormData();
    formData.append('post_id', postId);

    // Close Bootstrap modal
    $(`#post-modal-${postId}`).modal('hide')

    await fetch('/delete-post', {
        method: 'DELETE',
        body: formData
    });

    const gridItem = await document.getElementById(`post-grid-item-${postId}`);
    gridItem.parentNode.removeChild(gridItem);

    const modalItem = document.getElementById(`post-modal-${postId}`);
    modalItem.parentNode.removeChild(modalItem)

    let postCount = parseInt(document.getElementById("profile-post-count").innerText);
    let updatedPostCount = postCount - 1;

    document.getElementById('profile-post-count').innerText = updatedPostCount;

    if (updatedPostCount === 0) {
        document.getElementById("upload-first").classList.remove("invisible")
    }
}

$('.posts').infiniteScroll({
    path: function() {
            return `/next-feed`;
    },
    append: '.card',
    history: false
});

function previewImage(event) {
    const preview = document.getElementById('preview-image');
    preview.src = URL.createObjectURL(event.target.files[0]);
    preview.style.display = "block";
}

function commentReadMore(e) {
    const splicedCommentElement = e.parentElement;
    const fullCommentElement = $("#" + splicedCommentElement.getAttribute("id") + "> span.more-text");

    // Remove "... more"
    e.remove();

    const fullCommentText = fullCommentElement.text();
    fullCommentElement.remove();

    splicedCommentElement.innerText = fullCommentText
}

async function addComment(e) {
    const postId = await e.getAttribute('data-post-id');
    const component = await e.getAttribute('data-component');
    const comment = await document.getElementById(`comment-input-${postId}-${component}`);
    const commentText = comment.value;
    const postButton = $(`#btn-comment-submit-${postId}-${component}`);
    postButton.addClass('disabled');

    const formData = new FormData();
    formData.append('comment', commentText);
    formData.append('post_id', postId);

    const res = await fetch('/add-comment', {method: 'POST', body: formData})
    const commentHTML = await res.text();

    const div = document.createElement('div');
    div.innerHTML = commentHTML.trim();
    const cardCommentHTML = div.children[0];
    const modalCommentHTML = div.children[1];

    // Add comment to card
    const cardCommentList = document.getElementById(`comment-container-${postId}-card`);
    if (cardCommentList !== null && cardCommentList !== undefined) {
        cardCommentList.prepend(cardCommentHTML);
    }

    // Add comment to modal
    const modalCommentList = document.getElementById(`comment-container-${postId}-modal`);
    if (modalCommentList !== null && modalCommentList !== undefined) {
        modalCommentList.prepend(modalCommentHTML);
    }

    // const commentList = document.getElementById(`comment-container-${postId}-${component}`);
    // const div = document.createElement('div');
    // div.innerHTML = commentHTML.trim();
    // commentList.prepend(div);

    comment.value = '';

    // Update post comment count
    let postCommentCount = $(`#comment-count-${postId}`);
    postCommentCount.text(parseInt(postCommentCount.text())+1);
}

function changePostButtonState(e) {
    const postId = e.getAttribute('data-post-id');
    const component = e.getAttribute('data-component');
    const postButton = $(`#btn-comment-submit-${postId}-${component}`);

    if (e.value === "") {
        postButton.addClass('disabled');
    } else {
        postButton.removeClass('disabled');
    }
}