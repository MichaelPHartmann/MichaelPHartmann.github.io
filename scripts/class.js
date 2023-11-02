
import { posts } from "./posts.js";

export class MikeWebsite {
	constructor() {
		this.posts = posts;
		this.init();
	}

	/**
	* @description A function that creates a card that contains the details of the blog post
	* @param {string} index The index or ID of the post, typically the key from the posts object
	* @param {object} postObj The object body of the post
	* @return {node} The post card node
	*/
	createPostNode(index, postObj) {
		// Create the node that wraps the post card
		const node = document.createElement('div');
		node.id = index;
		node.classList = ['post'];
		// Create the title element to wrap the link
		const title = document.createElement('h3');
		// Create a link and attach the proper file
		const link = document.createElement('a');
		link.innerText = postObj.title;
		link.href = postObj.file;
		title.appendChild(link);
		// italicize the date
		const date = document.createElement('i');
		date.innerText = postObj.date;
		const description = postObj.description;
		// append everything to the wrapping node
		node.append(title, date, document.createElement('br'), description);
		return node;
	}

	/**
	* @description A function that paints post cards to a specified element
	* @param {string} id The id of the parent element into which the cards are painted
	* @param {string} tag Specifies a tag that all rendered posts must have to be rendered
	* @return undefined
	*/
	paintPosts(id, tag) {
		const target = document.getElementById(id);
		target.innerHTML = '';
		for (const post in this.posts) {
			if (!tag) {
				const node = this.createPostNode(post, this.posts[post]);
				target.appendChild(node);
			} else if (this.posts[post].tags.includes(tag)) {
				const node = this.createPostNode(post, this.posts[post]);
				target.appendChild(node);
			}
		}
	}

	/**
	* @description Counts instances of tags being used in blog posts
	* @return {object} The object of tags containing count information
	*/
	countTags() {
		if (this.tags) return this.tags;
		this.tags = {};
		for (const post in this.posts) {
			for (const tag of this.posts[post].tags) {
				if (this.tags[tag]) {
					this.tags[tag].count++;
				} else {
					this.tags[tag] = { count: 1 };
				}
			}
		}
		return this.tags;
	}

	/**
	* @description Paints the unique tags to the element with the `tags` id
	* @return undefined
	*/
	paintTags() {
		const target = document.getElementById('tags');
		for (const tag in this.tags) {
			const node = document.createElement('li');
			node.id = tag;
			const count = this.tags[tag].count;
			node.innerText = `${tag} [${count} post${count == 1 ? '' : 's'}]`;
			node.style.display = 'block';
			target.appendChild(node);
		}
	}

	listenToTags() {
		for (const tag in this.tags) {
			document.getElementById(tag).addEventListener('click', function(e) {
				console.log('Hello World', e);
				michaelhartmann.paintPosts('filtered', tag);
			})
		}
	}

	init() {
		this.paintPosts('posts');
		this.countTags();
		this.paintTags();
	}
}

window.michaelhartmann = new MikeWebsite();
