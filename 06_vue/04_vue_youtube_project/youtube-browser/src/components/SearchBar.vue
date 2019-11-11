<template>
    <div>
        <input @change="onInput" type="text"> <!-- input 될 때마다 함수를 실행시킨다.-->
    </div>
</template>

<script>
    export default {
        name: 'SearchBar',
        methods: {
            onInput(e) { // e: input값
                // 들어온 input을 부모로 올려줌 inputChange라는 이벤트와 함께 e.target.value 보내줌
                // 상위로 데이터 올려줌!
                this.$emit('inputChange', e.target.value) // this.$emit(eventname, args)
            }
        }
    }
</script>

<!-- scoped : SearchBar.vue에만 적용됨-->
<style scoped>
    input {
        width: 75%;
    }

    div {
        text-align: center;
        margin: 20px;
    }
</style>