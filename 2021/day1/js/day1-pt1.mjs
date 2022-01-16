import fetch from 'node-fetch';

let url='https://adventofcode.com/2021/day/1/input'
let cookie="session=53616c7465645f5f4de5a038aca9ce4b22a5552e1858981bc52ae2dd6ffbf026eac950be83e5270ff909e70e5b0e6f2b"

const opts = {
	headers: {
		cookie: "session=53616c7465645f5f4de5a038aca9ce4b22a5552e1858981bc52ae2dd6ffbf026eac950be83e5270ff909e70e5b0e6f2b"
	}
};

fetch(url, opts)
.then(response => response.text())
.then(data => {
	let depth = (data.split('\n'))
	let prev = 0
	var increase = 0
	let decrease = 0
	let window_size = 3
	let window_sum = 0
	for (let i = 0; i < depth.length - window_size; i++) {
		window_sum = parseInt(depth[i]) + parseInt(depth[i + 1]) + parseInt(depth[i + 2])
		if (i === 0) {
			prev = window_sum
			continue
		}
		if (window_sum > prev) {
			increase++
		} else if (window_sum < prev) {
			decrease++
		} else {
			// Unchanged depth
			continue
		}
		prev = window_sum
	}
	console.log('Total increases:' + increase);
})
