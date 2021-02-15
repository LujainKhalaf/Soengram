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
    let updatedPostCount = postCount-1;

    document.getElementById('profile-post-count').innerText = updatedPostCount;

    if (updatedPostCount == 0) {
        document.getElementById("upload-first").classList.remove("invisible")
    }

}