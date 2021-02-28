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
