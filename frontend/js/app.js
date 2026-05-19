// app.js
const API_BASE = "http://localhost:8000";

document.addEventListener("DOMContentLoaded", () => {
    const targetBtns = document.querySelectorAll(".target-btn");
    const convertBtn = document.getElementById("convertBtn");
    const copyBtn = document.getElementById("copyBtn");
    const inputText = document.getElementById("inputText");
    const outputText = document.getElementById("outputText");
    const loading = document.getElementById("loading");

    let selectedTarget = null;

    // 수신 대상 버튼 클릭 이벤트
    targetBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            targetBtns.forEach(b => b.classList.remove("active"));
            btn.classList.add("active");
            selectedTarget = btn.dataset.target;
        });
    });

    // 변환하기 버튼 클릭 이벤트
    convertBtn.addEventListener("click", async () => {
        const text = inputText.value.trim();

        if (!selectedTarget) {
            alert("수신 대상을 선택해주세요.");
            return;
        }

        if (!text) {
            alert("변환할 내용을 입력해주세요.");
            return;
        }

        setLoading(true);

        try {
            const response = await fetch(`${API_BASE}/api/convert`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    text: text,
                    target_audience: selectedTarget
                }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || "변환 중 오류가 발생했습니다.");
            }

            const data = await response.json();
            outputText.value = data.converted_text;
        } catch (error) {
            console.error("Error:", error);
            alert(error.message);
        } finally {
            setLoading(false);
        }
    });

    // 복사하기 버튼 클릭 이벤트
    copyBtn.addEventListener("click", () => {
        const text = outputText.value;
        if (!text) return;

        navigator.clipboard.writeText(text).then(() => {
            alert("클립보드에 복사되었습니다!");
        }).catch(err => {
            console.error("Copy failed:", err);
        });
    });

    function setLoading(isLoading) {
        if (isLoading) {
            loading.classList.remove("hidden");
            convertBtn.disabled = true;
            convertBtn.textContent = "변환 중...";
        } else {
            loading.classList.add("hidden");
            convertBtn.disabled = false;
            convertBtn.textContent = "변환하기";
        }
    }
});
