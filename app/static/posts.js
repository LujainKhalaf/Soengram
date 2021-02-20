async function deletePost(e) {
    const postId = await e.getAttribute('data-post-id');
    const formData = new FormData();
    formData.append('post_id', postId);
    await fetch('http://127.0.0.1:5000/delete', {
        method: 'POST',
        body: formData
    });
    const gridItem = await document.getElementById(`post-grid-item-${postId}`);
    gridItem.parentNode.removeChild(gridItem);

    let postCount = parseInt(document.getElementById("profile-post-count").innerText);
    let updatedPostCount = postCount - 1;

    document.getElementById('profile-post-count').innerText = updatedPostCount;

    if (updatedPostCount == 0) {
        document.getElementById("upload-first").classList.remove("invisible")
    }
}

async function follow(e) {
    let status = document.getElementById("follow-button").innerText;
    const thisUserId = await e.getAttribute('this-user-id');
    const formData = new FormData();
    formData.append('user_id', thisUserId);

    if (status == "Follow") {
        await fetch('http://127.0.0.1:5000/follow', {method: 'POST', body: formData});
        document.getElementById("follow-button").innerText = "Following";
        document.getElementById("follow-button").title = "Following";
        document.getElementById("follow-button").className = document.getElementById("follow-button").className.replace("btn-primary", "btn-following");
        document.getElementById("follow-button-follower-count").innerText = (parseInt(document.getElementById("follow-button-follower-count").innerText.valueOf()) + 1).toString();
    } else {
        await fetch('http://127.0.0.1:5000/unfollow', {method: 'POST', body: formData});
        document.getElementById("follow-button").innerText = "Follow";
        document.getElementById("follow-button").title = "Follow";
        document.getElementById("follow-button").className = document.getElementById("follow-button").className.replace("btn-following", "btn-primary");
        document.getElementById("follow-button-follower-count").innerText = (parseInt(document.getElementById("follow-button-follower-count").innerText.valueOf()) - 1).toString();
    }
}
