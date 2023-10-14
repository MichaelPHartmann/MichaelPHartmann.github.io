async function setRCMP() {
	const response = await fetch("https://csps.con.rcmp-grc.gc.ca/queryVehicles?vin=JS1VP52A6Y2102613", {
		"headers": {
			"accept": "application/json, text/javascript, */*; q=0.01",
			"accept-language": "en-US,en;q=0.9",
			"cache-control": "no-cache",
			"pragma": "no-cache",
			"sec-ch-ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
			"sec-ch-ua-mobile": "?0",
			"sec-ch-ua-platform": "\"Linux\"",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "cross-site"
		},
		"referrer": "https://www.cpic-cipc.ca/sve-rve-eng.htm",
		"referrerPolicy": "no-referrer-when-downgrade",
		"body": null,
		"method": "GET",
		"mode": "cors",
		"credentials": "omit"
	})
		.then(response => response.json())
		.then(json => {
			rcmp = JSON.stringify(json);
			document.getElementById('rcmp').innerHTML = rcmp;
		});
};

async function setICBC() {
	const response = await fetch("https://onlinebusiness.icbc.com/vdwqs/VDWQSServlet/FindVehicle", {
	"headers": {
		"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
		"accept-language": "en-US,en;q=0.9",
		"cache-control": "no-cache",
		"content-type": "application/x-www-form-urlencoded",
		"pragma": "no-cache",
		"sec-ch-ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
		"sec-ch-ua-mobile": "?0",
		"sec-ch-ua-platform": "\"Linux\"",
		"sec-fetch-dest": "document",
		"sec-fetch-mode": "navigate",
		"sec-fetch-site": "same-origin",
		"sec-fetch-user": "?1",
		"upgrade-insecure-requests": "1"
	},
	"referrer": "https://onlinebusiness.icbc.com/vdwqs/VDWQSServlet/FindVehicleForm?currentPage=0",
	"referrerPolicy": "strict-origin-when-cross-origin",
	"body": "vin=Js1vp52a6y2102613&year=2000&g-recaptcha-response=03AFcWeA6p60okLJHPPp4YQgWXxPm2h0AxoLMDbeUM4OdFXirjzmm95rs2MS96X7cJJO22C3D2WygkvnpWxOuiKHv4Y_7WI7QXUCvIo9eSMjS_QNob3eZBLQD5FJz_S1gs-DA5AcTixhcOOXc4e0_pjjhWeMFfu8yDP2C6jUKJZLmvqQganSq10Qszc4F_lYkVHKsjXGs9LfnOVmAhD1kdUX9f8T6dsvXP5twRMfsp6Kd8c6gFMFgmd9_cmTVagFZ-4S99ybK4EWV2JCCjwsi2hlTnGUf21XDTqIKMZrP-ur1WOpXwB5E6l4uANEkAb-gvYrEZYqxZfAS8c6Cdvq7yHgRtIrmNl6xucpDRVfY26MxuzohmBhR6XnEwa-iyNkBtvqdEdakndioKQoIt6o09hQqRji1U3GlpIcq6-ODVluk5_bE2FwS4_sy3QNmXuRik_4nh0WojqI8OA-JJP9_hQmkzyHW1v3Q-fahL1_VmEKY8GD-HmjWH3ks-1M49qEYkmP15Opa8pRExvaU_3Zw7_y_lCkBtiik3SSdWUi6Mo_0kVmRQDZMynGY&currentPage=1",
	"method": "POST",
	"mode": "cors",
	"credentials": "include"
	})
		.then((response) => {
			const result = response.text();
			const parser = new DOMParser();
			return parser.parseFromString(result, 'text/html');
		})
		.then((doc) => {
			const content = doc.getElementById('Content');
			const results = content.getElementsByClassName('queryResults')[0];
			const status = results.nextElementSibling.innerText;
			document.getElementById('icbc').innerHTML = status;
		});
};
