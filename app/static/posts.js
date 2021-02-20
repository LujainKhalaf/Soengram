async function deletePost(e) {
    const postId = await e.getAttribute('data-post-id');
    const formData = new FormData();
    formData.append('post_id', postId);

    // Close Bootstrap modal
    $('#post-modal-'+postId).modal('hide')

    await fetch('/delete', {
        method: 'POST',
        body: formData
    });
    const gridItem = await document.getElementById(`post-grid-item-${postId}`);
    gridItem.parentNode.removeChild(gridItem);


    var modalItem = document.getElementById(`post-modal-${postId}`);
    modalItem.parentNode.removeChild(modalItem)

    let postCount = parseInt(document.getElementById("profile-post-count").innerText);
    let updatedPostCount = postCount - 1;

    document.getElementById('profile-post-count').innerText = updatedPostCount;

    if (updatedPostCount == 0) {
        document.getElementById("upload-first").classList.remove("invisible")
    }
}

async function follow(e) {
    const userId = await e.getAttribute('this-user-id');
    const formData = new FormData();
    formData.append('user_id', userId);

    const followButton = document.getElementById('follow-button');
    const isFollowing = followButton.innerText === 'Follow';
    if (isFollowing) {
        await fetch('/follow', {method: 'POST', body: formData});
        followButton.innerText = 'Following';
        followButton.title = 'Following';
        followButton.className = 'btn btn-following';
    } else {
        await fetch('/unfollow', {method: 'POST', body: formData});
        followButton.innerText = 'Follow';
        followButton.title = 'Follow';
        followButton.className = 'btn btn-primary';
    }

    const followerCount = document.getElementById('follow-button-follower-count');
    const currentCount = parseInt(followerCount.innerText)
    followerCount.innerText = isFollowing ? `${currentCount + 1}` : `${currentCount - 1}`;
}
