const dark = {
	"primary-color": "#ebebeb",
	"bg-color": "#2f3437",
	"bg-color-dark": "#3f4447",
	"dark-trait": "#393c3f",
	"light-trait-100": "#3d4145",
	"light-trait-200": "#3d4145",
	"light-trait-300": "#72706b",
	"light-trait-400": "#37352f",
	"text-color": "#ebebeb",
	"text-color-secondary": "#73726e",
	"text-highlight-color": "#fff",
	"select-text-bg-color": "#2e5767",
	"search-select-text-color": "#eaedec",
	"search-select-bg-color": "#2e443a",
	"code-color": "#9a6e3a",
	"control-text-color": "#afb1b2",
	"item-hover-bg-color": "#4b5053",
	"active-file-bg-color": "#4b5053",
	"bg-codeblock": "#3f4447",
	"codeblock-text1": "#bde052",
	"codeblock-text2": "#d1949e",
};

const light = {
	"primary-color": "#37352f",
	"bg-color": "#ffffff",
	"bg-color-dark": "#f7f6f3",
	"dark-trait": "#e9e9e7",
	"light-trait-100": "#ecedec",
	"light-trait-200": "#c70000",
	"light-trait-300": "#37352f",
	"light-trait-400": "#f7f6f3",
	"text-color": "#37352f",
	"text-color-secondary": "#73726e",
	"text-highlight-color": "#fff",
	"select-text-bg-color": "#c0e5f4",
	"search-select-text-color": "#448361",
	"search-select-bg-color": "#edf3ec",
	"code-color": "#9a6e3a",
	"control-text-color": "#72706b",
	"item-hover-bg-color": "#e8e7e4",
	"active-file-bg-color": "#e8e7e4",
	"bg-codeblock": "#f7f6f3",
	"codeblock-text1": "#669900",
	"codeblock-text2": "#d1949e",
};

const setColorType = colors => {
	for (const [key, value] of Object.entries(colors)) {
		document.documentElement.style.setProperty(`--${key}`, `${value}`);
	}
};

const checkbox = document.getElementById("ChangeTheme");

if (sessionStorage.getItem("mode") == "dark") {
	darkmode();
} else {
	nodark();
}

checkbox.addEventListener("change", function () {
	checkbox.checked ? darkmode() : nodark();
});

function darkmode() {
	setColorType(dark);
	checkbox.checked = true;
	sessionStorage.setItem("mode", "dark");
}

function nodark() {
	setColorType(light);
	checkbox.checked = false;
	sessionStorage.setItem("mode", "light");
}
